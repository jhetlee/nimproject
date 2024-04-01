from django.contrib import admin
from django.urls import path
from nim_app import views
from django.conf.urls import url, include

app_name = 'nim_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^device/$', views.DeviceView.as_view(), name='device'),
    url(r'^device_create/$', views.DeviceCreateView.as_view(), name='device_create'),
    url(r'^datacenter/$', views.DataCenterView.as_view(), name='datacenter'),
    url(r'^datacenter/(?P<pk>\d+)/$',views.DCdevicesView.as_view(),name='data_center'),
    url(r'^device/(?P<pk>\d+)/$',views.InterfaceView.as_view(),name='interface'),
    url(r'^device/interface_create/$',views.InterfaceCreateView.as_view(),name='interface_view'),
    url(r'^update/(?P<pk>\d+)/$',views.DeviceUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeviceDeleteView.as_view(),name='delete'),
    url(r'via_client/$', views.VIAClientView.as_view(), name='via_client')

]
