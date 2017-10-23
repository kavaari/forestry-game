from django.shortcuts import render
from django.http import JsonResponse
from forestry_game.models import CustomUser, Level, Report
from forestry_game.serializers import CustomUserSerializer, LevelSerializer, ReportSerializer

from rest_framework import generics

class UserCreateView(generics.ListCreateAPIView):
	queryset = Level.objects.all()
	serializer_class = LevelSerializer
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

def home ( request ):
    context = dict()
    return render(request, 'index.html', context)
