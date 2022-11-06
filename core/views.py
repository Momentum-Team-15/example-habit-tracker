from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def habit_list(request):
    habits = request.user.habits.all()
    return render(
        request,
        "habit_tracker/habit_list.html",
        {
            "habits": habits,
            "form": forms.HabitForm(),
            "bulma_classes": [
                "is-primary",
                "is-link",
                "is-warning",
                "is-info",
                "is-success",
                "is-danger",
            ],
        },
    )


@login_required
def habit_new(request):
    if request.method == "POST":
        form = forms.HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habit_list")

    return render(request, "habit_tracker/habit_new.html", {"form": HabitForm()})
