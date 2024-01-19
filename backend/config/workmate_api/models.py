from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

class Schedule(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event, blank=True)
    tasks = models.ManyToManyField(Task, blank=True)
    goals = models.ManyToManyField(Goal, blank=True)
    day_intervals = models.JSONField(default=dict)

class UserInsight(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    success_rate = models.FloatField(default=0.0)
    total_time_spent_on_tasks = models.DurationField(default=0)
    tasks_completed_before_deadline = models.PositiveIntegerField(default=0)
    total_tasks = models.PositiveIntegerField(default=0)