from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_challenge, name='random_challenge'),
    path('complete/<int:challenge_id>/', view)  