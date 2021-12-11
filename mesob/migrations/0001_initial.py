# Generated by Django 3.2.9 on 2021-12-11 00:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('number_of_guests', models.IntegerField()),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
