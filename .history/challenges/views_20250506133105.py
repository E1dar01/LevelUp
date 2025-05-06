import random
from django.shortcuts import render, redirect
from .models import Challenge, UserChallenge

def random_challenge(request):
    if not request.uswer.is_authenticated:
        return redirect('login')
    challenge = random.choice(Challenge.objects.all())
    return render(request, 'challenges/ra
