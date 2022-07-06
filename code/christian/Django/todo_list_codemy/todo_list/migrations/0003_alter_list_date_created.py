# Generated by Django 4.0.5 on 2022-07-06 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_list_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
