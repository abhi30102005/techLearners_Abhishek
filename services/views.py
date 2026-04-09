from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import json
from django.http import JsonResponse
from .models import Provider, Booking
from .models import Review
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Provider, Booking
from django.contrib.auth.decorators import login_required

def home(request):
    skill = request.GET.get('skill')

    if skill:
        providers = Provider.objects.filter(skill__iexact=skill)
    else:
        providers = Provider.objects.all()

    return render(request, "index.html", {
        "providers": providers
    })

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('/')
    
    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=email, email=email, password=password)
        return redirect('/login/')

    return render(request, "signup.html")
def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request, "profile.html")
from .models import Booking

def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request,
     "booking_history.html", {"bookings": bookings})



@login_required
def book_service(request):
    if request.method == "POST":
        data = json.loads(request.body)

        provider_id = data.get("provider_id")
        time = data.get("time")

        provider = Provider.objects.get(id=provider_id)

        Booking.objects.create(
            user=request.user,
            provider=provider,
            time=time
        )

        return JsonResponse({"status": "success"})

def add_review(request):
    if request.method == "POST":
        data = json.loads(request.body)

        booking_id = data.get("booking_id")
        rating = data.get("rating")
        comment = data.get("comment")

        booking = Booking.objects.get(id=booking_id)

        Review.objects.create(
            booking=booking,
            user=request.user,
            provider=booking.provider,
            rating=rating,
            comment=comment
        )

        return JsonResponse({"status": "review added"})
    
def add_provider(request):
    if request.method == "POST":
        name = request.POST['name']
        skill = request.POST['skill']
        rate = request.POST['rate']
        location = request.POST['location']

        # ✅ FIX: update if exists, else create
        provider, created = Provider.objects.update_or_create(
            user=request.user,
            defaults={
                "name": name,
                "skill": skill,
                "rate": rate,
                "location": location
            }
        )

        return redirect('/provider-dashboard/')

    return render(request, "add_provider.html")

def provider_dashboard(request):
    try:
        provider = Provider.objects.get(user=request.user)
    except Provider.DoesNotExist:
        return redirect('/become-pro/')

    bookings = Booking.objects.filter(provider=provider)

    total_bookings = bookings.count()
    total_earnings = total_bookings * 500

    return render(request, "provider_dashboard.html", {
        "bookings": bookings,
        "total_bookings": total_bookings,
        "total_earnings": total_earnings
    })
