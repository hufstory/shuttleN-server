
from django.contrib import admin
from django.urls import path
from shuttle import views

urlpatterns = [
    path('getBusLoc/',views.getBusLoc)

]
