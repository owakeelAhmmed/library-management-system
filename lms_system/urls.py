from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to Library API"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
