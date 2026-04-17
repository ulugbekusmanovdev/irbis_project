from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostuplenyForm
from .models import *

# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def home_page(request):
    books = Postupleny.objects.all()
    

    context = {'books': books}
    return render(request, 'home.html', context)

def addBook(request):
    post_form = PostuplenyForm(prefix='post')
    

    if request.method == 'POST':
        post_form = PostuplenyForm(request.POST, prefix='post')
       

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()
            return redirect('home')

    return render(request, 'addBook.html', {
        'post_form': post_form,
    
    })

def editBook(request,pk):

    post = get_object_or_404(Postupleny, id=pk)
    

    if request.method == 'POST':
        form = PostuplenyForm(request.POST, instance=post)
        
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = PostuplenyForm(instance=post)
        

    return render(request, 'editBooks.html', {
        'form': form,
      
    })
