from django.contrib import admin
from nim_app.models import DataCenter, Devices, Interface, VIA_clients
# Register your models here.


admin.site.register(DataCenter)
admin.site.register(Devices)
admin.site.register(Interface)
admin.site.register(VIA_clients)