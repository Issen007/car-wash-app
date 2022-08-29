from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings

app_name = 'issassist'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path(r'', HomeView.as_view(), name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
