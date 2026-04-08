from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=50)
    rate = models.CharField(max_length=20)
    rating = models.CharField(max_length=10)
    reviews = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    avatar_initials = models.CharField(max_length=2)

    def __str__(self):
        return self.name

# NEW: The table that actually saves the user's booking
class Booking(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100, default="Guest User")
    time_slot = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking: {self.provider.name} at {self.time_slot}"