from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
import requests,json

# Forms
from .forms import EmailForm

from .models import EmailSettings
from . import email

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

        context = {
            'title' : 'Settings',
            'header' : 'ArPix',
            'email' : email
        }
        return render(request, template_name, context)

class EmailCreateView(CreateView):
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
        email_address = json.loads(response)
        text = email.notification(registration_number='ABC123')
        text.email(email=email_address['email_address'])
        
        return HttpResponseRedirect(reverse_lazy('notification:home'))
        
def Delete(request, id):
    '''
    Delete SMTP Settings from our database
    '''
    url = "http://localhost:8000/api/v1/email/" + str(id) + "/"
    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse_lazy('notification:home'))

# class EmilSettingsView(FormView):
#     def get(self, request, *args, **kwargs):
#         template_name = 'email.html'
        

#         context = {
#             'title' : 'Settings',
#             'header' : 'ArPix',
#             'data' : data
#         }

#         return render(request, template_name, context)

#     def post(self, request, *args, **kwargs):
#         form = EmailForm
#         url = "http://localhost:8000/api/v1/email/"
       
#         headers = {
#             'Content-Type': 'application/json'
#         }
        
#         payload = json.dumps({
#             "work_type": request.POST['work_type'],
#         })
        
#         response = requests.request("POST", url, headers=headers, data=payload)
#         return HttpResponseRedirect(reverse('settings'))
