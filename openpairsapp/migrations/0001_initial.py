# Generated by Django 3.0.7 on 2020-06-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=15, null=True)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(max_length=6, null=True)),
                ('region', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('year_group', models.CharField(max_length=10, null=True)),
                ('temperature', models.IntegerField(null=True)),
                ('sleep', models.IntegerField(null=True)),
                ('sleep_school_time', models.IntegerField(null=True)),
                ('sleep_weekend_time', models.IntegerField(null=True)),
                ('wakeup_school_time', models.IntegerField(null=True)),
                ('wakeup_weekend_time', models.IntegerField(null=True)),
                ('sleep_light', models.IntegerField(null=True)),
                ('room_brightness_day', models.IntegerField(null=True)),
                ('room_brightness_night', models.IntegerField(null=True)),
                ('noise', models.IntegerField(null=True)),
                ('sleep_noise', models.IntegerField(null=True)),
                ('clean_room', models.IntegerField(null=True)),
                ('private_time', models.IntegerField(null=True)),
                ('meditate', models.IntegerField(null=True)),
                ('conversational', models.IntegerField(null=True)),
                ('sharing', models.IntegerField(null=True)),
                ('day_visitors', models.IntegerField(null=True)),
                ('night_visitors', models.IntegerField(null=True)),
                ('visiting_time', models.IntegerField(null=True)),
                ('quiet_space', models.IntegerField(null=True)),
                ('allergies', models.IntegerField(null=True)),
                ('brush', models.IntegerField(null=True)),
                ('laundry', models.IntegerField(null=True)),
                ('shower', models.IntegerField(null=True)),
                ('room_decor', models.IntegerField(null=True)),
            ],
        ),
    ]
