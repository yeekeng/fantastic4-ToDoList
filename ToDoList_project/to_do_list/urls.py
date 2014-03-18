from django.conf.urls import patterns, url
from to_do_list import views

urlpatterns = patterns('',
        url(r'^$', views.login, name='login'),
        url(r'^register/$', views.register, name='register'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^mainpage/$', views.mainpage, name='mainpage'),
        url(r'^createtask/$', views.createtask, name='createtask'),
        url(r'^viewgroup/(?P<group_name_url>\w+)/$', views.viewgroup, name='viewgroup'),
        url(r'^edittask/(?P<task_id_url>\w+)/$', views.edittask, name='edittask'),





)
