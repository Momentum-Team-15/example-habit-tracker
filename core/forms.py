from django import forms
from .models import Habit, DailyRecord


class DatePickerInput(forms.DateInput):
    input_type = "date"


class HabitForm(forms.ModelForm):
    # https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#styling-widget-instances
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "input"})
        self.fields["metric"].widget.attrs.update({"class": "input"})
        self.fields["unit_of_measure"].widget.attrs.update({"class": "input"})

    class Meta:
        model = Habit
        fields = ("name", "metric", "unit_of_measure")
        labels = {
            "name": "What habit do you want to build?",
            "metric": "What is your target number for daily reps of this habit?",
            "unit_of_measure": "Unit of measure",
        }


class DailyRecordForm(forms.ModelForm):
    habit_pk = forms.IntegerField(widget=forms.HiddenInput(), required=False, label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["amount"].widget.attrs.update({"class": "input"})
        self.fields["date"].widget.attrs.update({"class": "input"})

    class Meta:
        model = DailyRecord
        fields = ("date", "amount", "habit_pk")
        widgets = {"date": DatePickerInput()}
