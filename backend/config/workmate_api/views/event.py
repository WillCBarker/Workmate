import workmate_api.models as m
import workmate_api.serializers as s

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from datetime import timedelta


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
            serializer.validated_data["user"] = current_user
            new_event = serializer.save()

            user_schedule, created = m.Schedule.objects.get_or_create(user=current_user)
            user_schedule.events.add(new_event)

            start_time = new_event.start_datetime
            end_time = new_event.end_datetime
            interval = timedelta(minutes=15)

            while start_time < end_time:
                start_key = start_time.strftime("%H:%M")

                if start_key not in user_schedule.day_intervals:

                    user_schedule.day_intervals[start_key] = []
                user_schedule.day_intervals[start_key].append(new_event.id)

                start_time += interval

            user_schedule.save()

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