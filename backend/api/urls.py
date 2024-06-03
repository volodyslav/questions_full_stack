
from django.contrib import admin
from django.urls import path, include
from main.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    # User register
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    # Refresh and access tokens
    path("api/user/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    
    path("api-auth/", include("rest_framework.urls")),
    # Main api
    path("api/", include("main.urls")),
]
