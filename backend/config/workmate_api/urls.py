from django.urls import path
import workmate_api.views as v

urlpatterns = [
    path("goals/", v.Goals.as_view(), name="goals"),
    path("goals/<int:pk>/", v.Goals.as_view(), name="goal_detail"),

    path("user_insights/", v.UserInsight.as_view(), name="user_insights"),
    path("user_insights/<int:pk>/", v.UserInsight.as_view(), name="user_insight_detail"),

    path("tasks/", v.Tasks.as_view(), name="tasks"),
    path("tasks/<int:pk>/", v.Tasks.as_view(), name="task_detail"),

    path("schedule/", v.Schedule.as_view(), name="schedule"),
    path("schedule/<int:pk>/", v.Schedule.as_view(), name="schedule_detail"),

    path("events/", v.Events.as_view(), name="events"),
    path("events/<int:pk>/", v.Events.as_view(), name="event_detail"),
]