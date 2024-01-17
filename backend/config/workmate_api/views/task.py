import workmate_api.models as m
import workmate_api.serializers as s

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class Tasks(APIView):
    def get(self, request):
        """ Get all tasks for a given user """

        current_user = request.user

        objs = m.Task.objects.all().filter(user=current_user)

        serializer = s.TaskSerializer(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ Create a new task """
        
        current_user = request.user

        serializer = s.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = current_user
            serializer.save()
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