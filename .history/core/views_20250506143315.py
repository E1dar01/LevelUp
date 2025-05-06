from challenges.models import UsersChallenge
from django.shortcuts import render

def leaderboard(request):
    total_completed = UsersChallenge
    return render(request, 'core/leaderboard.html', {