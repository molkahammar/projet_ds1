from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Hello, CI/CD!"})

# Create your views here.
