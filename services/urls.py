from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view),
    path('signup/', views.signup_view),
    path('logout/', views.logout_view),  # ✅ NEW
    path('profile/', views.profile),
    path('api/book/', views.book_service),
    path('provider-dashboard/', views.provider_dashboard),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/review/', views.add_review),
    path('become-pro/', views.add_provider),
]