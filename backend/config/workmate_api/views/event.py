import workmate_api.models as m
import workmate_api.serializers as s

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class Events(APIView):
    def get(self, request):
        """ Get all events for a given user """

        current_user = request.user

        objs = m.Event.objects.all().filter(user=current_user)

        serializer = s.EventSerializer(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_detail(self, request, pk):
        current_user = request.user
        try:
            obj = m.Event.objects.get(pk=pk, user=current_user)
            serializer = s.EventSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except m.Event.DoesNotExist:
            return Response({"detail": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        """ Create a new event """
        
        current_user = request.user

        serializer = s.EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = current_user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """ Update an event by ID """

        current_user = request.user

        try:
            obj = m.Event.objects.get(pk=pk, user=current_user)
        except m.Event.DoesNotExist:
            return Response({"detail": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = s.EventSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """ Delete an event by ID """

        current_user = request.user

        try:
            obj = m.Event.objects.get(pk=pk, user=current_user)
        except m.Event.DoesNotExist:
            return Response({"detail": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"detail": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)