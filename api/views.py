from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Habit
from .serializers import HabitSerializer

class HabitListView(APIView):

  def get(self, request, format=None):
        """
        Return a list of all habits.
        """
        # query for all the habits
        habits = Habit.objects.all()
        # serialize the data so that I can return habits as json
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

  def post(self, request, format=None):
    """Create a new habit.

        Need the pk of an existing user for this.
        The IsAuthenticatedOrReadOnly permission class (set in settings) will
        ensure that I have a logged in user.
    """
    # the body of the request has the info to create a new habit
    serializer = HabitSerializer(data=request.data)
    if serializer.is_valid():
        # if that all checks out, we still need to associate the user
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
