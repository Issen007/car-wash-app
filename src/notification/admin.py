from django.contrib import admin

# Register your models here.
from .models import EmailSettings

class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = [
        'smtp_server',
        'smtp_port',
        'smtp_user',
        'smtp_password',
        ]

    class Meta:
        model = EmailSettings
admin.site.register(EmailSettings, EmailSettingsAdmin)
