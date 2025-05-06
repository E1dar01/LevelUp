from django.contrib.auth.decorators import User 
from challenges.models import UsersChallenge
from django.db.models import Sum, Count
from django.shortcuts import render

def leaderboard(request):
    users = User.objects.annotate(
