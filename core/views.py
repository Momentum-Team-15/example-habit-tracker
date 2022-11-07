import datetime
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Habit, DailyRecord

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


@login_required
def habit_detail(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)

    return render(request, "habit_tracker/habit_detail.html", {"habit": habit})


@login_required
def habit_daily_record(request, habit_pk=None, year=None, month=None, day=None):
    habit = get_object_or_404(Habit, pk=habit_pk)
    view_context = {"habit": habit}
    if year is None:
      date = datetime.date.today()
    else:
      date = datetime.date(year, month, day)

    daily_record, created = habit.records.get_or_create(date=date)

    if created:
        form_header_text = "Record your results for today."
    else:
        form_header_text = "You've already recorded results today. Update them?"

    if request.method == 'POST':
      form = forms.DailyRecordForm(data=request.POST, instance=daily_record)
      form_header_text = "You've already recorded results today. Update them?"
      if form.is_valid():
          daily_record = form.save(commit=False)
          daily_record.habit = habit
          try:
            daily_record.save()
          except IntegrityError:
            error_msg="A record already exists for this date"
    else:
      form = forms.DailyRecordForm(
            initial={"date": daily_record.date, "habit_pk": habit.pk, "amount": daily_record.amount}
        )

    view_context.update(
        form=form,
        daily_record=daily_record,
        habit=habit,
        form_header_text=form_header_text
    )

    return render(request, "habit_tracker/habit_results.html", view_context)
