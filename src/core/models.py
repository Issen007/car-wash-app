# Django Apps
from django.db import models
from django.conf import settings

# Create your models here.

class work(models.Model):
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    registration_number = models.CharField(max_length = 16, default = 'ABC123', blank=False)
    finish_time = models.DateTimeField(auto_now = False, auto_now_add = False)
    started = models.BooleanField(default = False)
    completed = models.BooleanField(default = False)
    status = models.CharField(max_length = 16, default = '', blank=True)
    work_type = models.CharField(max_length = 256, default = '', blank=True)
    email_address = models.CharField(max_length = 128, default = 'name@company.com', blank=True)
    email_notification = models.BooleanField(default = False)
    phonenumber = models.CharField(max_length = 20, default = '070111222', blank=True)
    sms_notification = models.BooleanField(default = False)

    def __str__(self):
        return str(self.work)

class workType(models.Model):
    work_type = models.CharField(max_length = 128, default = 'Tvätt', blank=True)
