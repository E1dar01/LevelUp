from challenges.models import UsersChallenge
from django.shortcuts import render

def leaderboard(request):
    total_completed = 
    return render(request, 'core/leaderboard.html', {'users': users})
