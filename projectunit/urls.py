from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projectunit-home'),
    path('about/', views.about, name='projectunit-about'),
]
