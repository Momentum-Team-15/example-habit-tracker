from django.contrib import admin
from .models import User, Habit, DailyRecord
# Register your models here.
admin.site.register(User)
admin.site.register(Habit)
admin.site.register(DailyRecord)
