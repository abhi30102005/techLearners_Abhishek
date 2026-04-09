from django.db import models
from django.contrib.auth.models import User

# Service Provider
class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    rate = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.provider.name}"
    
class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    rating = models.IntegerField()  # 1–5
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)