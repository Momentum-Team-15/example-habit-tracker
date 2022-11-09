"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from api import views as api_views

urlpatterns = [
    path("", views.habit_list, name="habit_list"),
    path("habits/", views.habit_list, name="habit_list"),
    path("habits/new", views.habit_new, name="habit_new"),
    path("habits/<int:habit_pk>", views.habit_detail, name="habit_detail"),
    path(
        "habits/<int:habit_pk>/records",
        views.habit_daily_record,
        name="habit_records",
    ),
    path(
        "habit/<int:habit_pk>/records/<int:year>/<int:month>/<int:day>",
        views.habit_daily_record,
        name="habit_daily_record",
    ),
    path('api-auth/', include('rest_framework.urls')),
    path("admin/", admin.site.urls),
    path("auth/", include("registration.backends.simple.urls")),
    path("api/habits/", api_views.HabitListView.as_view(), name="api-habit-list"),
]
