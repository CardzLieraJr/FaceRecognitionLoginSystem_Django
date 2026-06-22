from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Face Recognition System is running")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]