from challenges.models import UsersChallenge
from django.shortcuts import render

def leaderboard(request):
    
    return render(request, 'core/leaderboard.html', {'users': users})
