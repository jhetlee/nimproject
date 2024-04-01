from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
# Create your models here.


class DataCenter(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("nim_app:data_center", kwargs={'pk':self.pk})

class Devices(models.Model):
    device_name = models.CharField(max_length=256)
    rack_location = models.CharField(max_length=256, null=True, blank=True, default='')
    oob_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    datacenter = models.ForeignKey(DataCenter, related_name='dc', on_delete=models.CASCADE)
    def __str__(self):
        return self.device_name
    def get_absolute_url(self):
        return reverse("nim_app:device")

class Interface(models.Model):
    interface_number = models.CharField(max_length=256)
    interface_description = models.CharField(max_length=256)
    interface_detail = models.CharField(max_length=256, null=True, blank=True, default='')
    devices = models.ForeignKey(Devices, related_name='devices', on_delete=models.CASCADE)
    def __str__(self):
        return self.interface_number + " - " + self.interface_description
    def get_absolute_url(self):
        return reverse("nim_app:device")


class VIA_clients(models.Model):
    datacenter = models.ForeignKey(DataCenter, related_name='datacenter', on_delete=models.CASCADE)
    VIP = models.CharField(max_length=256)
    primary_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    secondary_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    client_name = models.CharField(max_length=256)
    sr_number = models.CharField(max_length=256)
    bandwidth = models.CharField(max_length=256)

    def __str__(self):
        return self.client_name




