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