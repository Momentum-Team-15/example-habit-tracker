from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Habit(BaseModel):
    name = models.CharField(max_length=255)
    metric = models.PositiveIntegerField()
    unit_of_measure = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")

    def __str__(self):
        return self.name


class DailyRecord(BaseModel):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")
    amount = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["date", "habit"], name="unique_daily_record_for_habit"
            )
        ]

    def __str__(self):
        return f"Record for {self.habit.name} on {self.date.strftime('%A %D')}"
