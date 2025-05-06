from challenges.models import UsersChallenge
from django.shortcuts import render

def leaderboard(request):
    total_points=Sum('userschallenge__challenge__points'),
        completed_challenges=Count('userschallenge')
    ).order_by('-total_points')
    return render(request, 'core/leaderboard.html', {'users': users})
