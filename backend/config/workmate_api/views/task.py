import workmate_api.models as m
import workmate_api.serializers as s

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from datetime import timedelta


class Tasks(APIView):
    def get(self, request):
        """ Get all tasks for a given user """

        current_user = request.user

        objs = m.Task.objects.all().filter(user=current_user)

        serializer = s.TaskSerializer(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_detail(self, request, pk):
        current_user = request.user
        try:
            obj = m.Task.objects.get(pk=pk, user=current_user)
            serializer = s.TaskSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except m.Task.DoesNotExist:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        """ Create a new task """
        
        current_user = request.user

        serializer = s.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = current_user
            new_task = serializer.save()

            user_schedule, created = m.Schedule.objects.get_or_create(user=current_user)
            user_schedule.events.add(new_task)

            start_time = new_task.start_datetime
            end_time = new_task.end_datetime
            interval = timedelta(minutes=15)

            while start_time < end_time:
                start_key = start_time.strftime("%H:%M")

                if start_key not in user_schedule.day_intervals:
                    user_schedule.day_intervals[start_key] = []
                user_schedule.day_intervals[start_key].append(new_task.id)

                start_time += interval

            user_schedule.save()


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """ Update a task by ID """

        current_user = request.user

        try:
            obj = m.Task.objects.get(pk=pk, user=current_user)
        except m.Task.DoesNotExist:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = s.TaskSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """ Delete a task by ID """

        current_user = request.user

        try:
            obj = m.Task.objects.get(pk=pk, user=current_user)
        except m.Task.DoesNotExist:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"detail": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)