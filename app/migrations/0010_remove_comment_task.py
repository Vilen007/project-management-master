# Generated by Django 3.2.6 on 2021-09-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210918_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='task',
        ),
    ]
