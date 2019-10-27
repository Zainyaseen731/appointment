# Generated by Django 2.2.5 on 2019-10-22 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0003_auto_20191021_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentTimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_day', models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=1)),
                ('appointment_time', models.TimeField()),
            ],
        ),
    ]