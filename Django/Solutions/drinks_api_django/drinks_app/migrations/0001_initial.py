# Generated by Django 3.2.7 on 2022-05-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=50)),
                ('drink_url', models.CharField(max_length=100)),
                ('favourite', models.BooleanField(default=False)),
            ],
        ),
    ]