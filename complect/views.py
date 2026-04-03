from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def home_page(request):
    return render(request, 'home.html')
