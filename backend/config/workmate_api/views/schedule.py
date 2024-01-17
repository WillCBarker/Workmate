import workmate_api.models as m
import workmate_api.serializers as s

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class Schedule(APIView):
    def get(self, request):
        """ Get schedule of a given user """

        current_user = request.user

        obj = m.Schedule.objects.all().filter(user=current_user)

        serializer = s.ScheduleSerializer(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """ Create a new schedule """
        
        current_user = request.user

        serializer = s.ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = current_user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """ Update a schedule by ID """

        current_user = request.user

        try:
            obj = m.Schedule.objects.get(pk=pk, user=current_user)
        except m.Schedule.DoesNotExist:
            return Response({"detail": "Schedule not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = s.ScheduleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """ Delete a schedule by ID """

        current_user = request.user

        try:
            obj = m.Schedule.objects.get(pk=pk, user=current_user)
        except m.Schedule.DoesNotExist:
            return Response({"detail": "Schedule not found"}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"detail": "Schedule deleted successfully"}, status=status.HTTP_204_NO_CONTENT)