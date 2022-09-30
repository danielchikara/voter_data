from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from apps.api.views import *
app_name = 'api'
router = routers.DefaultRouter()
router.register('leader', UserLeaderViewSet , basename='leader')
router.register('voter', UserVoterViewSet , basename='voter')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
