from forestry_game.models import Level, Report
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = User 
		fields = ('id', 'username', 'password')

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data["password"])
		user.save()
		return user

class LoginSerializer(serializers.ModelSerializer):

	class Meta:
		model = User 
		fields = ('id', 'username', 'email', 'password')

class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = ('id', 'name', 'timestamp', 'last_edited', 'mapdata', 'creator')

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = ('id', 'timestamp', 'distance', 'gas_consumption', 'duration', 'logs', 'user', 'level')
