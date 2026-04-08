from django.contrib import admin
from .models import Provider, Booking

admin.site.register(Provider)
admin.site.register(Booking) # This lets you see bookings in 127.0.0.1:8000/admin