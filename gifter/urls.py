from django.conf.urls import patterns, include, url
from django.contrib import admin
from lamps import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add-list/$', views.add_list, name='add-list'),
    url(r'^add-gifts/$', views.add_gifts, name='add-gifts'),
    url(r'^edit-gifts/$', views.buy, name='buy'),
    url(r'^login/$', views.custom_login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^my-lists/$', views.my_list_view, name='my-lists'),
    url(r'^my-lists/(?P<slug>[-\w\d]+),(?P<lid>\d+)/$', views.list_detail, name='list-detail'),
    url(r'^edit-gifts/(?P<slug>[-\w\d]+)/$', views.buy, name='edit-gifts'),
    url(r'^admin/', include(admin.site.urls)),
)
