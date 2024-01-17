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