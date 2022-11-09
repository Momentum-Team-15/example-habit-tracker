from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, generics
from .serializers import HabitSerializer


# If you use APIView, you need to write your own handler methods like `get` and `post`
class HabitBasicListView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request, format=None):
        """
        Return a list of all habits for a logged in user.
        """
        # query for all the habits
        habits = request.user.habits.all()
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



# If you use Generic Views, you get CRUD methods for free (i.e., you write less code!)
# https://www.cdrf.co/3.13/rest_framework.generics/ListCreateAPIView.html
class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # by overriding this method, I can filter habits by the logged in user
        return self.request.user.habits.all()

    def perform_create(self, serializer):
        # by overriding this method, I can associate the user who is creating this habit
        serializer.save(user=self.request.user)
