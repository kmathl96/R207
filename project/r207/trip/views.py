from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Register your models here.
def index(request):
    return render(request, 'index.html')
