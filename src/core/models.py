# Django Apps
from django.db import models
from django.conf import settings

# Create your models here.

class work(models.Model):
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    registration_number = models.CharField(max_length = 16, default = 'ABC123', blank=False)
    # work = models.ForeignKey(workType, default = 1, on_delete=models.CASCADE)
    finish_time = models.DateTimeField(auto_now = False, auto_now_add = False)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return str(self.work)

class workType(models.Model):
    work_type = models.CharField(max_length = 128, default = 'DISK', blank=True)
