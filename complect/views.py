from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def main_page1(request):
    return render(request, 'main.html')