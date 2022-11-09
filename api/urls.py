from django.urls import path
from . import views

urlpatterns = [
  path("habits/", views.HabitListCreateView.as_view(), name="api-habit-list"),
]
