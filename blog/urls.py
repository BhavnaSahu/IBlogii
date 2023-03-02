from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
   path("home/",home),
   path('blog/<slug:url>', post),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
