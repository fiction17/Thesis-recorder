# Generated by Django 3.0.5 on 2021-03-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]