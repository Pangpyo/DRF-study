# Generated by Django 4.1.3 on 2022-11-28 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="courser",
            new_name="course",
        ),
    ]
