from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  pass


class Habit(models.Model):
  name=models.CharField(max_length=255)
  metric=models.PositiveIntegerField()
  unit_of_measure=models.CharField(max_length=255)
  description=models.TextField(null=True, blank=True)
  user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")

  def __str__(self):
      return self.name

class DailyRecord(models.Model):
  habit=models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")
  date=models.DateField(auto_now_add=True)
  amount=models.PositiveIntegerField()

  def __str__(self):
      return f"Record for {self.habit.name}"
