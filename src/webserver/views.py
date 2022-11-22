from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse

# from urllib import response
import requests, json
from datetime import datetime, timezone, timedelta
from notification import message

import logging
log = logging.getLogger(__name__)

class ViewMode(View):
    '''
    This is a view mode only for our worker to understand what to do next
    '''
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
            i['emergency'] = False
            utc_dt = datetime.now(timezone.utc)
            now = utc_dt.astimezone() + timedelta(hours=1)
            if (finish_time < now):
                i['emergency'] = True

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
    '''
    Our view to manage all our customer orders
    '''
    def get(self, request, *args, **kwargs):
        template_name = 'home.html'
        url = "http://localhost:8000/api/v1/work"
        response = requests.request("GET", url)
        work = json.loads(response.text)
        work_string = json.loads(response.text)
        for i in work:
            timestamp = datetime.strptime(i['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z')
            finish_time = datetime.strptime(i['finish_time'], '%Y-%m-%dT%H:%M:%S%z')
            i['timestamp'] = timestamp
            i['finish_time'] = finish_time
            i['emergency'] = False
            utc_dt = datetime.now(timezone.utc)
            now = utc_dt.astimezone() + timedelta(hours=1)
            if (finish_time < now):
                i['emergency'] = True
        
        for i in work_string:
            timestamp = datetime.strptime(i['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z')
            finish_time = datetime.strptime(i['finish_time'], '%Y-%m-%dT%H:%M:%S%z')
            timestamp = timestamp.strftime('%Y-%m-%d %H:%M')
            finish_time = finish_time.strftime('%Y-%m-%d %H:%M')
            i['timestamp'] = timestamp
            i['finish_time'] = finish_time
            i['emergency'] = False        
                
        work_url = "http://localhost:8000/api/v1/work_type/"
        work_response = requests.request("GET", work_url)

        work_type = json.loads(work_response.text)

        print(work_string)

        context = {
            'title' : 'ArPix',
            'header' : 'ArPix',
            'work' : work_string,
            'work_type': work_type,
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
            value_check['email_address'] = 'info@foo.local'
                    
        if not 'send_sms' in value_check:
            value_check['send_sms'] = False
            value_check['phonenumber'] = '0701234567'

        if 'phonenumber' in value_check:
            phone_value = value_check['phonenumber']
            if phone_value[0] == '0':
                phone_value = phone_value.replace(phone_value[0], '+46', 1)
                value_check['phonenumber'] = phone_value
    
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
    '''
    Here is all our settings for all our work types
    '''
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
        url = "http://localhost:8000/api/v1/work_type/"
       
        headers = {
            'Content-Type': 'application/json'
        }
        
        payload = json.dumps({
            "work_type": request.POST['work_type'],
        })
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return HttpResponseRedirect(reverse('work'))

def Started(request, id):
    '''
    We will only update our work that is has started
    '''
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

def Edit(request, id):
    '''
    We will only update our work that is has started
    '''
    url = "http://localhost:8000/api/v1/work/" + str(id) + "/"
    payload = {}

    headers = {
        'Content-Type': 'application/json'
    }
    print(json.dumps(request.POST, indent=4))
    
    # response = requests.request("GET", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse('home'))


def Complete(request, id):
    '''
    This function is when the user have press Completed work.
    Here will we update status for our work to Completed, but also notify our customer
    via Email or/and SMS
    '''
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
        '''
        Email Messaging via smtplib library
        '''
        log.info('Send Email to ' + work_id['email_address'] + ' for car ' + work_id['registration_number'] )
        note = message.notification(registration_number=work_id['registration_number'])
        note.email(email=work_id['email_address'])

    if work_id['sms_notification']:
        '''
        SMS Text Message Service via Twilio API
        '''
        log.info('Send SMS to ' + work_id['phonenumber'] + ' for car ' + work_id['registration_number'])
        note = message.notification(registration_number=work_id['registration_number'])
        note.sms(phonenumber=work_id['phonenumber'])

    return HttpResponseRedirect(reverse('home'))

def Delete(request, id):
    '''
    Our work is completed and the customer has collect its car
    We will delete the work from our database
    '''
    url = "http://localhost:8000/api/v1/work/" + str(id) + "/"
    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse('home'))

def WorkDelete(request, id):
    '''
    Here are we removing a type of work from our worklist
    '''
    url = "http://localhost:8000/api/v1/work_type/" + str(id) + "/"
    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return HttpResponseRedirect(reverse('work'))
