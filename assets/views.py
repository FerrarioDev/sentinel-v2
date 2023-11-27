from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def add_asset(request):
    return render(request, 'assets/index.html')
