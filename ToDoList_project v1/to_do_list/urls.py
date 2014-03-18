from django.conf.urls import patterns, url
from to_do_list import views

urlpatterns = patterns('',
        url(r'^$', views.login, name='login'),
        url(r'^mainpage/$', views.mainpage, name='mainpage'),
        url(r'^register/$', views.register, name='register'),


)
