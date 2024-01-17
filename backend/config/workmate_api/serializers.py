from rest_framework import serializers
from .models import Goal, Event, Task, Schedule, UserInsight

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class UserInsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInsight
        fields = '__all__'
