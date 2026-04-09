from django.contrib import admin
from .models import Provider, Booking, Review

admin.site.register(Provider)
admin.site.register(Booking)
admin.site.register(Review)