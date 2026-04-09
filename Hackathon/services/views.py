from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Provider, Booking
import json

def home(request):
    providers = Provider.objects.all()
    return render(request, 'index.html', {'providers': providers})

# NEW: Hackathon API Endpoint
@csrf_exempt # Bypasses security checks so we can build fast
def book_service(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            provider_id = data.get('provider_id')
            time_slot = data.get('time')
            
            # Find the provider and save the booking
            provider = Provider.objects.get(id=provider_id)
            Booking.objects.create(
                provider=provider,
                time_slot=time_slot
            )
            
            return JsonResponse({'status': 'success', 'message': 'Saved to DB!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'invalid method'})