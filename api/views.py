from rest_framework.views import APIView
from rest_framework.response import Response
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


def habit_list(request):
  # get the habits
  habits = Habit.objects.all()
  # return the response
  return render(request, "path-to-template", {"habits": habits})
