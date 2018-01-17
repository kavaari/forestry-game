from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate, login, logout as django_logout

from django.contrib.auth.models import User
from forestry_game.models import Level, Report
#from forestry_game.serializers import LevelSerializer, MapInfoSerializer, MapDataSerializer, ReportSerializer, RegisterSerializer, LoginSerializer
from forestry_game.serializers import *
from rest_framework import generics

import json

from .forms import RegisterForm
from .svg import generateSVG


class RegisterView(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		form = RegisterForm(request.POST)
		if form.is_valid():
			self.create(request, *args, **kwargs)
			user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
			if user is None:
				return HttpResponse(status=401)
			else:
				login(request, user)
				return JsonResponse({
					'username': user.username,
					'email': user.email
				}, safe=False)
		else:
			formErrors = form.errors.as_data()
			errors = []
			if 'username' in formErrors:
				for err in formErrors['username']:
					if 'This field is required.' in err.messages[0]:
						errors.append('usernameRequired')
					if 'Ensure this value has at least' in err.messages[0]:
						errors.append('usernameTooShort')
					if 'Ensure this value has at most' in err.messages[0]:
						errors.append('usernameTooLong')
			if 'email' in formErrors:
				for err in formErrors['email']:
					if 'This field is required.' in err.messages[0]:
						errors.append('emailRequired')
					if 'Enter a valid email address.' in err.messages[0]:
						errors.append('emailInvalid')
			if 'password' in formErrors:
				for err in formErrors['password']:
					if 'This field is required.' in err.messages[0]:
						errors.append('passwordRequired')
					if 'Ensure this value has at least' in err.messages[0]:
						errors.append('passwordTooShort')
					if 'Ensure this value has at most' in err.messages[0]:
						errors.append('passwordTooLong')

			return JsonResponse(errors, safe=False, status=400)

class LoginView(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializer_class = LoginSerializer

	def post(self, request):
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is None:
			return HttpResponse(status=401)
		else:
			login(request, user)
			return JsonResponse({
				'username': user.username,
				'email': user.email
			}, safe=False)

class LevelView(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	serializer_class = LevelSerializer

	def get_queryset(self):
		queryset = Level.objects.all()
		if self.request.method == 'GET':
			id = self.request.query_params.get('id', None)
			if id is not None:
				queryset = Level.objects.filter(pk = id)
			else:
				onlyUser = self.request.query_params.get('user', None)
				if onlyUser == '1':
					if self.request.user.is_authenticated():
						queryset = Level.objects.filter(creator = self.request.user)
					else:
						return None
		return queryset

	def get(self, request, *args, **kwargs):

		if request.GET.get('id', False):
			self.serializer_class = MapDataSerializer
		else:
			self.serializer_class = MapInfoSerializer

		response = self.list(request, *args, **kwargs)
		for row in response.data:
			if 'mapinfo' in row:
				row['mapinfo'] = json.loads(row['mapinfo'])
			if 'mapdata' in row:
				row['mapdata'] = json.loads(row['mapdata'])
		return response

	def post(self, request):
		if request.path == '/api/v1/level/delete':
			print (request.path)
			if request.user.is_authenticated():
				if 'id' in request.POST:
					level = get_object_or_404(Level, pk=request.POST['id'])
					level.delete()
					return HttpResponse(status=200)
				else:
					return HttpResponse(status=400)
			else:
				return HttpResponse(status=403)
		else:
			if request.user.is_authenticated():
				level = Level()
				level.name = request.POST['levelName']
				level.mapdata = request.POST['mapData']
				level.mapinfo = request.POST['mapInfo']
				level.creator = request.user
				level.save()
				return JsonResponse({
					'id': level.pk
				}, safe=False)
			return HttpResponse(status=403)

class LevelUpdateView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = LevelSerializer

	def post(self, request):
		if request.user.is_authenticated():
			level = get_object_or_404(Level, pk=request.POST['id'])
			level.mapdata = request.POST['mapData']
			level.mapinfo = request.POST['mapInfo']
			level.creator = request.user
			level.save()
			return JsonResponse({
				'id': level.pk
			}, safe=False)
		return HttpResponse(status=403)

class ReportView(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	serializer_class = ReportSerializer

	def get_queryset(self):
		queryset = Report.objects.all()
		if self.request.method == 'GET':
			if not self.request.user.is_superuser:
				id = self.request.query_params.get('n', None)
				if id is not None:
					queryset = Report.objects.filter(pk = id)
				elif self.request.user.is_authenticated():
					queryset = Report.objects.filter(user = self.request.user).order_by('-timestamp')
		return queryset

	def get(self, request, *args, **kwargs):
		response = self.list(request, *args, **kwargs)
		for row in response.data:
			if 'logs' in row:
				row['logs'] = json.loads(row['logs'])
		return response

	def post(self, request):
		if request.user.is_authenticated():
			report = Report()
			report.distance = request.POST['distance']
			report.timestamp = request.POST['enddate']
			report.gas_consumption = request.POST['fuel']
			report.duration = request.POST['time']
			report.logs = request.POST['logs']
			report.user = request.user
			report.level = get_object_or_404(Level, pk=request.POST['id'])

			report.driving_unloaded_time = request.POST['driving_unloaded_time']
			report.driving_loaded_time = request.POST['driving_loaded_time']
			report.loading_and_unloading = request.POST['loading_and_unloading']
			report.idling = request.POST['idling']

			report.driving_forward = request.POST['driving_forward']
			report.reverse = request.POST['reverse']
			report.driving_unloaded_distance = request.POST['driving_unloaded_distance']
			report.driving_loaded_distance = request.POST['driving_loaded_distance']
			
			report.fuel_cost = request.POST['fuel_cost']
			report.worker_salary = request.POST['worker_salary']
			report.loads_transported = request.POST['loads_transported']
			report.logs_deposited = request.POST['logs_deposited']
			report.total_volume = request.POST['total_volume']
			report.productivity = request.POST['productivity']
			report.save()
			return HttpResponse(status=200)
		return HttpResponse(status=403)

@permission_classes((IsAuthenticated,))
def logoutView(request):
	django_logout(request)
	return HttpResponse(status=200)

@ensure_csrf_cookie
@permission_classes((AllowAny,))
def validate( request ):
	if request.user.is_authenticated():

		return JsonResponse({
			'username': request.user.username,
			'email': request.user.email
		}, safe=False)

	return HttpResponse(status=204)

@ensure_csrf_cookie
def home ( request ):
    context = dict()
    return render(request, 'index.html', context)

def levelImageView(request, id):
	level = get_object_or_404(Level, pk=id)
	mapdata = json.loads(level.mapdata)
	mapImage = generateSVG(mapdata)

	response = HttpResponse(mapImage)
	response['Content-Type'] = 'image/svg+xml'
	response['Cache-control'] = 'max-age=0, must-revalidate, no-store'

	return response
