from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
import requests,json

from .models import EmailSettings, SMSSettings
from . import message

class NotificationView(View):
    '''
    Get a full status view of all Text Messages and E-Mail Settings
    '''
    def get(self, request, *args, **kwargs):
        template_name = 'notification/home.html'
        url = "http://localhost:8000/api/v1/email/"
       
        headers = {
            'Content-Type': 'application/json'
        }
        
        payload = {}
        
        response = requests.request("GET", url, headers=headers, data=payload)
        email = json.loads(response.text)
        
        url = "http://localhost:8000/api/v1/sms/"
        response = requests.request("GET", url, headers=headers, data=payload)
        sms = json.loads(response.text)

        context = {
            'title' : 'Settings',
            'header' : 'ArPix',
            'email' : email,
            'sms' : sms
        }
        return render(request, template_name, context)

class EmailCreateView(CreateView):
    '''
    Setup your Email SMTP Settings
    '''
    template_name = 'notification/email_form.html'
    model = EmailSettings
    success_url = reverse_lazy('notification:home')
    fields = [
        'smtp_server',
        'smtp_port',
        'smtp_user',
        'smtp_password',
        'smtp_subject',
        'smtp_body'
    ]

class EmailUpdateView(UpdateView):
    '''
    Update your Email Settings
    '''
    template_name = 'notification/email_form.html'
    model = EmailSettings
    success_url = reverse_lazy('notification:home')
    fields = [
        'smtp_server',
        'smtp_port',
        'smtp_user',
        'smtp_password',
        'smtp_subject',
        'smtp_body'
    ]

class EmailTestView(View):
    '''
    This is a test function to verify if you email settings are correct.
    '''
    def post(self, request, *args, **kwargs):
        response = json.dumps(request.POST)
        response = json.loads(response)
        text = message.notification(registration_number='ABC123')
        text.email(email=response['email_address'])
        
        return HttpResponseRedirect(reverse_lazy('notification:home'))
        
def EmailDelete(request, id):
    '''
    Delete SMTP Settings from our database
    '''
    url = "http://localhost:8000/api/v1/email/" + str(id) + "/"
    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse_lazy('notification:home'))

class SMSCreateView(CreateView):
    '''
    Setup SMS Settings
    '''
    template_name = 'notification/email_form.html'
    model = SMSSettings
    success_url = reverse_lazy('notification:home')
    fields = [
        'account_sid',
        'auth_token',
        'message_sid',
        'country_code',
        'phonenumber',
        'body'
    ]

class SMSUpdateView(UpdateView):
    '''
    Update your SMS Settings
    '''
    template_name = 'notification/email_form.html'
    model = SMSSettings
    success_url = reverse_lazy('notification:home')
    fields = [
        'account_sid',
        'auth_token',
        'message_sid',
        'country_code',
        'phonenumber',
        'body'
    ]

class SMSTestView(View):
    '''
    This is a test function to verify if you SMS Service are correct.
    '''
    def post(self, request, *args, **kwargs):
        print(request.POST)
        response = json.dumps(request.POST)
        response = json.loads(response)
        text = message.notification(registration_number='ABC123')
        text.sms(phonenumber=response['phonenumber'])
        
        return HttpResponseRedirect(reverse_lazy('notification:home'))
        
def SMSDelete(request, id):
    '''
    Delete SMS Settings from our database
    '''
    url = "http://localhost:8000/api/v1/sms/" + str(id) + "/"
    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse_lazy('notification:home'))
