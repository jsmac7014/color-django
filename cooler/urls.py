from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout,login
from django.conf import settings

urlpatterns = [
    url(r'^$', views.color_list, name='color_list'),
    url(r'^make', views.color_new, name='color_make'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login',login, {'template_name': 'cooler/login.html'}, name='login'), 
    url(r'^logout',logout ,{'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'), 
]