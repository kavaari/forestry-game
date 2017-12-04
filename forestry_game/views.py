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

from .svg import generateSVG


class RegisterView(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		#TODO: Check if user creation fails and handle it properly
		self.create(request, *args, **kwargs)
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is None:
			return HttpResponse(status=401)
		else:
			login(request, user)
			return JsonResponse({
				'username': user.username,
				'email': user.email
			}, safe=False)

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

	return response
