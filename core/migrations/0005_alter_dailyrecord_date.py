# Generated by Django 4.1.3 on 2022-11-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_dailyrecord_created_at_dailyrecord_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyrecord",
            name="date",
            field=models.DateField(),
        ),
    ]
