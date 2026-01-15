from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Redirect root URL to admin login page
    path('', RedirectView.as_view(url='/admin/login/', permanent=False)),

    # Django admin
    path('admin/', admin.site.urls),

    # JWT authentication
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Employee APIs
    path('api/employees/', include('employees.urls')),
]

