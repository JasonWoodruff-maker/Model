# Generated by Django 5.1.2 on 2024-11-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="first_name",
            field=models.CharField(default="default", max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="last_name",
            field=models.CharField(default="default", max_length=30),
            preserve_default=False,
        ),
    ]
