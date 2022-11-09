from rest_framework import serializers
from core.models import Habit

class HabitSerializer(serializers.ModelSerializer):
  class Meta:
    model = Habit
    fields = ["id", "name", "metric", "unit_of_measure", "user"]
