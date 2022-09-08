# Django Apps
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class EmailSettings(models.Model):
    
    class EncryptionType(models.TextChoices):
        STARTTLS = 'STLS', _('STARTTLS')
        TLS = 'TLS', _('TLS')
        NONE = 'NONE', _('NONE')

    smtp_server = models.CharField(max_length = 64, default = 'smtp.google.com', blank=False)
    smtp_port = models.IntegerField(default = 587, blank = False)
    smtp_user = models.CharField(max_length = 128, default = 'name@company.com', blank=True)
    smtp_password = models.CharField(max_length = 256, default = 'password', blank=True)
    smtp_protocol = models.CharField(max_length = 4, choices=EncryptionType.choices, default=EncryptionType.STARTTLS)
    smtp_subject = models.TextField(max_length = 64, default = 'Default E-Mail Subject Title', blank=True)
    smtp_body = models.TextField(max_length = 255, default = 'Default Body Field', blank=True)


    def __str__(self):
        return str(self.smtp_server)
