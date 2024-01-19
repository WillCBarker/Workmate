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
    
    def get_detail(self, request, pk):
        current_user = request.user
        try:
            obj = m.Goal.objects.get(pk=pk, user=current_user)
            serializer = s.GoalSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except m.Goal.DoesNotExist:
            return Response({"detail": "Goal not found"}, status=status.HTTP_404_NOT_FOUND)

    
    def post(self, request):
        """ Create a new goal """

        current_user = request.user

        serializer = s.GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["user"] = current_user
            new_goal = serializer.save()

            user_schedule, created = m.Schedule.objects.get_or_create(user=current_user)
            user_schedule.events.add(new_goal)

            deadline = new_goal.deadline
            deadline_key = deadline.strftime("%H:%M")

            if deadline_key not in user_schedule.day_intervals:
                user_schedule.day_intervals[deadline_key] = []
            user_schedule.day_intervals[deadline_key].append(new_goal.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """ Update a goal by ID """

        current_user = request.user

        try:
            obj = m.Goal.objects.get(pk=pk, user=current_user)
        except m.Goal.DoesNotExist:
            return Response({"detail": "Goal not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = s.GoalSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """ Delete a goal by ID """

        current_user = request.user

        try:
            obj = m.Goal.objects.get(pk=pk, user=current_user)
        except m.Goal.DoesNotExist:
            return Response({"detail": "Goal not found"}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"detail": "Goal deleted successfully"}, status=status.HTTP_204_NO_CONTENT)