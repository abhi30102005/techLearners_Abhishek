from django.contrib import admin
from django.urls import path
from services.views import home, book_service

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/book/', book_service, name='book_service'), # NEW API ROUTE
]