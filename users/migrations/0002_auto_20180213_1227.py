# Generated by Django 2.0.2 on 2018-02-13 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='delete_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='register_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
