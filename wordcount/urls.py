from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.home),
    path('count/', views.count),

]
