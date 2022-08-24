# Generated by Django 3.2.6 on 2021-09-04 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='domain_name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='progression',
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.state'),
        ),
    ]
