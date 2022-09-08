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
    path(r'', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('add/', HomeView.as_view(), name='add_work'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('started/<int:id>', Started, name='started'),
    path('complete/<int:id>', Complete, name='complete'),
    path('delete/<int:id>', Delete, name='delete'),
    path('work_type/add/', SettingsView.as_view(), name='add_work_type'),
    path('work_type/delete/<int:id>', WorkDelete, name='work_delete'),
    path('view/', ViewMode.as_view(), name='view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
