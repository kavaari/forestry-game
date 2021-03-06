from forestry_game.models import Level, Report
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email')

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data["password"])
		user.save()
		return user

class LoginSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')

# LEVELSERIALIZER NOT IN USE RIGHT NOW
class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = ('id', 'name', 'timestamp', 'last_edited', 'mapdata', 'mapinfo', 'creator')

class MapInfoSerializer(serializers.ModelSerializer):
	creator = serializers.CharField(source='creator.username', read_only=True)

	class Meta:
		model = Level
		fields = ('id', 'name', 'mapinfo', 'creator', 'last_edited')

class MapDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = ('id', 'name', 'mapdata')

class ReportSerializer(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)
	level = serializers.CharField(source='level.name', read_only=True)
	m_score = serializers.CharField(source='score', read_only=True)
	class Meta:
		model = Report
		fields = ('id', 'timestamp', 'distance',
			'gas_consumption', 'duration', 'logs',
			'user', 'level', 'm_score',
			'driving_unloaded_time', 'driving_loaded_time',
			'loading_and_unloading', 'idling', 'driving_forward',
			'reverse', 'driving_unloaded_distance', 'driving_loaded_distance',
			'fuel_cost', 'worker_salary', 'loads_transported',
			'logs_deposited', 'total_volume', 'productivity')
		