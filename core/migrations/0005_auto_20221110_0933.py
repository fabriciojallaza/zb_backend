# Generated by Django 3.2.16 on 2022-11-10 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
