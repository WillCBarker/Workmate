import workmate_api.models as m
import workmate_api.serializers as s

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class Goals(APIView):
    def get(self, request):
        """ Get all goals for a given user """

        current_user = request.user

        objs = m.Goal.objects.all().filter(user=current_user)

        serializer = s.GoalSerializer(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)