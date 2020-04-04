from django.contrib import admin
from django.urls import path, include
from microsoftCalApp import views

urlpatterns = [
    path('microsoftCalApp/', include('microsoftCalApp.urls')),
    path('admin/', admin.site.urls),
]