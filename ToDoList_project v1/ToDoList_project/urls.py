from django.conf.urls import patterns, include, url



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:s
    # url(r'^$', 'ToDoList_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^to_do_list/', include('to_do_list.urls')), # ADD THIS NEW TUPLE

)
