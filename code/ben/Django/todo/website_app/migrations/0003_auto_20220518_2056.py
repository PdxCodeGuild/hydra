# Generated by Django 3.2.9 on 2022-05-19 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0002_auto_20220517_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=500)),
                ('create_date', models.DateField()),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
