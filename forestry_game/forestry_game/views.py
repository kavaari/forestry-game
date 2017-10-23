from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from forestry_game.models import Level, Report
from forestry_game.serializers import LevelSerializer, ReportSerializer, UserSerializer
from rest_framework import generics



class UserCreateView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	print(serializer_class)

	def create_user(self, serializer):
		serializer.save()

class LevelCreateView(generics.ListCreateAPIView):
	queryset = Level.objects.all()
	serializer_class = LevelSerializer
	print(serializer_class)

	def create_level(self, serializer):
		serializer.save()

class ReportCreateView(generics.ListCreateAPIView):
	queryset = Level.objects.all()
	serializer_class = LevelSerializer
	print(serializer_class)

	def create_report(self, serializer):
		serializer.save()

@ensure_csrf_cookie
def csrf( request ):
	return HttpResponse(status=200)

def home ( request ):
    context = dict()
    return render(request, 'index.html', context)

def register( request ):
		request
