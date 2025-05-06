from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_challenge, name='random_challenge'),
    path('complete/<int:challenge_id>/', views.complete_challenge, name='complete_challenge')<  