from django.urls import path

from .views import (
    NotificationView,
    EmailCreateView,
    EmailUpdateView,
    EmailTestView,
    Delete,
)

app_name = 'notification'

urlpatterns = [
    path(r'', NotificationView.as_view(), name='home'),
    path(r'email/create', EmailCreateView.as_view(), name='email_create'),
    path(r'email/update/<int:pk>', EmailUpdateView.as_view(), name='email_update'),
    path(r'email/delete/<int:id>', Delete, name='email_delete'),
    path(r'email/test', EmailTestView.as_view(), name='email_test'),

]
