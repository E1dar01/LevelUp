import random
from django.shortcuts import render, redirect
from .models import Challenge, UserChallenge

def random_challenge(request):
    if not request.uswer
