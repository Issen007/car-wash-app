from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from .views import (
    HomeView,
    SettingsView,
    Started,
    Complete,
    Delete,
    WorkDelete,
    ViewMode,
)

app_name = 'webserver'

urlpatterns = [
    path(r'home/', HomeView.as_view(), name='home'),
    path(r'admin/', admin.site.urls),
    path(r'api/', include('api.urls')),
    path(r'add/', HomeView.as_view(), name='add_work'),
    path(r'settings/work', SettingsView.as_view(), name='work'),
    path(r'settings/notification/', include('notification.urls')),
    path(r'started/<int:id>', Started, name='started'),
    path(r'complete/<int:id>', Complete, name='complete'),
    path(r'delete/<int:id>', Delete, name='delete'),
    path(r'work_type/add/', SettingsView.as_view(), name='add_work_type'),
    path(r'work_type/delete/<int:id>', WorkDelete, name='work_delete'),
    path(r'', ViewMode.as_view(), name='view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
