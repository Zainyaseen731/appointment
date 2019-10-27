from enum import Enum

from django.db import models
from django.db.models.signals import post_save,pre_save
from .validator import valid_email
from django.utils.text import slugify
from django.utils.timesince import timesince
from datetime import timedelta,datetime,date


class Appointment(models.Model):
    first_name = models.CharField(max_length=30, default="Zain")
    last_name = models.CharField(max_length=30, default="Yaseen")
    email = models.CharField(max_length=40,validators=[valid_email], default="zain@gmail.com")
    note = models.TextField(max_length=500,default="Comming soon .....")
    date=models.DateField(auto_now=False,auto_now_add=False)
    time=models.TimeField(auto_now=False,auto_now_add=False,default='00:00')
    status=models.BooleanField(default=0)
    num=models.CharField(max_length=1,default=0.0)


    def __str__(self):
        return (self.first_name)


class AppointmentTimeSlot(models.Model):

    class DaysOfWeek(Enum):
        Monday = '0'
        Tuesday = '1'
        Wednesday = '2'
        Thursday = '3'
        Friday = '4'
        Saturday = '5'
        Sunday = '6'

        @classmethod
        def model_choices(cls):
            return tuple([(attr.value, attr.name) for attr in cls])

    appointment_day = models.CharField(max_length=1, choices=DaysOfWeek.model_choices())
    appointment_time = models.TimeField()


    def __str__(self):
        return (self.appointment_day)

