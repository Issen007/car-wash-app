from django.urls import path

from .views import (
    NotificationView,
    EmailCreateView,
    EmailUpdateView,
    EmailTestView,
    EmailDelete,
    SMSCreateView,
    SMSUpdateView,
    SMSDelete,
    SMSTestView,
)

app_name = 'notification'

urlpatterns = [
    path(r'', NotificationView.as_view(), name='home'),
    path(r'email/create', EmailCreateView.as_view(), name='email_create'),
    path(r'email/update/<int:pk>', EmailUpdateView.as_view(), name='email_update'),
    path(r'email/delete/<int:id>', EmailDelete, name='email_delete'),
    path(r'email/test', EmailTestView.as_view(), name='email_test'),
    path(r'sms/create', SMSCreateView.as_view(), name='sms_create'),
    path(r'sms/update/<int:pk>', SMSUpdateView.as_view(), name='sms_update'),
    path(r'sms/delete/<int:id>', SMSDelete, name='sms_delete'),
    path(r'sms/test', SMSTestView.as_view(), name='sms_test'),

]
