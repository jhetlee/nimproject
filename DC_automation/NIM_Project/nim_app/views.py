from urllib import request
from nim_app.forms import  InterfaceForm
from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from . import models
from django.http import HttpResponseForbidden
from django.urls import reverse
from nim_app import forms
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView, FormView)

from django.http import HttpResponse

# Create your views here.
from .models import Interface, Devices, DataCenter, VIA_clients

class IndexView(TemplateView):
    template_name = 'index.html'

class DeviceView(ListView):
    context_object_name = 'device_list'
    model = models.Devices
    template_name = 'devices.html'

class DataCenterView(ListView):
    context_object_name = 'datacenter'
    model = models.DataCenter
    template_name = 'data_center.html'

class DCdevicesView(DetailView):
    context_object_name = 'dc_devices'
    model = models.DataCenter
    template_name = 'dc_device.html'

class InterfaceView(DetailView):
    context_object_name = 'interfaces'
    model = models.Devices
    template_name = 'interfaces.html'
    queryset = Devices.objects.all()
    print(queryset)

class VIAClientView(ListView):
    context_object_name = 'clients'
    model = models.VIA_clients
    template_name = 'via_clients.html'

class DeviceCreateView(CreateView):
    template_name = 'device_create_form.html'
    context_object_name = 'create_device'
    fields = ['device_name', 'rack_location', 'oob_address', 'datacenter']
    model = models.Devices
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class InterfaceCreateView(CreateView):
    context_object_name = 'interfaces'
    fields = ['devices','interface_number', 'interface_description', 'interface_detail']
    model = models.Interface
    template_name = 'interface_create_form.html'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class DeviceUpdateView(UpdateView):
    fields = fields = ['device_name', 'rack_location', 'oob_address']
    model = models.Devices
    template_name = 'update_form.html'

class DeviceDeleteView(DeleteView):
    context_object_name = 'device'
    model = models.Devices
    success_url = reverse_lazy("nim_app:device")
    template_name = 'confirm_delete.html'


class Interface_CreateView(FormMixin, DetailView):
    context_object_name = 'device'
    model = models.Devices
    template_name = 'interface_create_form.html'
    form_class = InterfaceForm
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            print('valid')
            return self.form_valid(form)
        else:
            print('invalid')
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)









