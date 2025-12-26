from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome, you're at the root of the Youthacks Portal")