# Generated by Django 3.2.6 on 2021-09-17 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='user',
        ),
    ]
