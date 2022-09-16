# Django Default Modules
from django.conf.urls import include #We will try to remove url
from django.urls import path
from rest_framework import routers
#from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

# Apps specific
from .views import (
    WorkViewSet, 
    WorkTypeViewSet,
    EmailViewSet,
    )

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'work', WorkViewSet, basename = 'work')
router.register(r'work_type', WorkTypeViewSet, basename = 'work_type')
router.register(r'email', EmailViewSet, basename = 'email')

urlpatterns = [
    #url(r'v1/get-token-auth/', views.obtain_auth_token), ### Get my token for each user ###
    path('v1/', include(router.urls)),
    # path('auth/', include('dj_rest_auth.urls')),
    # path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
