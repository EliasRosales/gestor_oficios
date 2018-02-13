from django.conf.urls import url

from users.api.views import login

urlpatterns = [
    url(r'^login/$', login, name='api_login_user'),
]