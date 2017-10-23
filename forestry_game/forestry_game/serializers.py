from forestry_game.models import CustomUser, Level, Report
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id', 'user')

class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = ('id', 'name', 'timestamp', 'last_edited', 'mapdata', 'creator')

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = ('id', 'timestamp', 'distance', 'gas_consumption', 'duration', 'logs', 'user', 'level')
