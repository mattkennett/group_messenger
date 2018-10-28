# Imports from Django
from django.conf.urls import include, url
from django.contrib import admin

# Imports from Django Rest Framework
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

# Imports from messenger app
from messenger import views

router = routers.DefaultRouter()
router.register(r'^api/channels', views.ChannelViewSet)
router.register(r'^api/messages', views.MessageViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/v1/', include('rest_auth.urls')),
    url(r'^api-auth/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api-token-auth/v1/', authtoken_views.obtain_auth_token),
    url(r'^', include('messenger.urls')),
]
