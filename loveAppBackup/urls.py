from django.contrib import admin
from django.urls import path
from django.urls import include, path
from loveAppBackup import views

urlpatterns = [
    path('Neha/', admin.site.urls),
    path('', views.wait, name = 'wait')
]
