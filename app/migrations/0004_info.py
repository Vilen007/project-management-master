# Generated by Django 3.2.6 on 2021-08-22 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_task_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('port', models.IntegerField()),
                ('domain_name', models.URLField()),
                ('version', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=200, null=True)),
                ('backup', models.BooleanField(default=True, verbose_name='Backup')),
                ('file', models.FileField(blank=True, upload_to='upload')),
                ('git', models.CharField(max_length=200)),
                ('notes', models.TextField(default='notes')),
                ('project_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
    ]
