# Generated by Django 4.0.6 on 2022-07-26 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone2_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='claim',
        ),
    ]
