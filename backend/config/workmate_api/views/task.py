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

