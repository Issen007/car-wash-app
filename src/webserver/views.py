from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse

# from urllib import response
import requests, json
from datetime import datetime
from notification import email

class ViewMode(View):
    def get(self, request, *args, **kwargs):
        template_name = 'view.html'
        url = "http://localhost:8000/api/v1/work/"
        response = requests.request("GET", url)
        work = json.loads(response.text)
        for i in work:
            timestamp = datetime.strptime(i['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z')
            finish_time = datetime.strptime(i['finish_time'], '%Y-%m-%dT%H:%M:%S%z')
            i['timestamp'] = timestamp
            i['finish_time'] = finish_time
            now = datetime.now()
            print('*' * 100)
            print(timestamp.hour)
            print(now.hour)

        work_url = "http://localhost:8000/api/v1/work_type/"
        work_response = requests.request("GET", work_url)

        work_type = json.loads(work_response.text)

        context = {
            'title' : 'ArPix',
            'header' : 'ArPix',
            'work' : work,
            'work_type': work_type
        }

        return render(request, template_name, context)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'home.html'
        url = "http://localhost:8000/api/v1/work/"
        response = requests.request("GET", url)
        work = json.loads(response.text)
        for i in work:
            timestamp = datetime.strptime(i['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z')
            finish_time = datetime.strptime(i['finish_time'], '%Y-%m-%dT%H:%M:%S%z')
            i['timestamp'] = timestamp
            i['finish_time'] = finish_time
            now = datetime.now()

        work_url = "http://localhost:8000/api/v1/work_type/"
        work_response = requests.request("GET", work_url)

        work_type = json.loads(work_response.text)

        context = {
            'title' : 'ArPix',
            'header' : 'ArPix',
            'work' : work,
            'work_type': work_type
        }

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        url = "http://localhost:8000/api/v1/work/"

        headers = {
            'Content-Type': 'application/json'
        }
        
        data = json.dumps(request.POST)
        value_check = json.loads(data)
        if not 'send_email' in value_check:
            value_check['send_email'] = False
        
        if not 'send_sms' in value_check:
            value_check['send_sms'] = False

        payload = json.dumps({
            "registration_number": value_check['registration_number'],
            "email_address": value_check['email'],
            "email_notification": value_check['send_email'],
            "phonenumber": value_check['phonenumber'],
            "sms_notification": value_check['send_sms'],
            "finish_time": value_check['finish_time'],
            "work_type": value_check['work_type']
        })
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return HttpResponseRedirect(reverse('home'))

class SettingsView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'settings.html'
        url = "http://localhost:8000/api/v1/work_type/"
        response = requests.request("GET", url)
        data = json.loads(response.text)
        print(data)
        context = {
            'title' : 'Settings',
            'header' : 'ArPix',
            'data' : data
        }

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        url = "http://localhost:8000/api/v1/work_type/"
       
        headers = {
            'Content-Type': 'application/json'
        }
        
        payload = json.dumps({
            "work_type": request.POST['work_type'],
        })
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return HttpResponseRedirect(reverse('settings'))

def Started(request, id):
    url = "http://localhost:8000/api/v1/work/" + str(id) + "/"
    payload = json.dumps({ 
        "started": True,
        "completed": False,
        "status": 'PÅ BÖRJAD'
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse('home'))

def Complete(request, id):
    url = "http://localhost:8000/api/v1/work/" + str(id) + "/"
    payload = json.dumps({ 
        "started": True,
        "completed": True,
        "status": 'KLAR'
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    work_data = requests.request("GET", url)
    work_id = json.loads(work_data.text)
    
    if work_id['email_notification']:
        print('Send Email to ' + work_id['email_address'] + ' for car ' + work_id['registration_number'] )
        note = email.notification(registration_number=work_id['registration_number'])
        note.email(email=work_id['email_address'])

    return HttpResponseRedirect(reverse('home'))

def Delete(request, id):
    url = "http://localhost:8000/api/v1/work/" + str(id) + "/"
    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse('home'))

def WorkDelete(request, id):
    url = "http://localhost:8000/api/v1/work_type/" + str(id) + "/"
    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse('settings'))
