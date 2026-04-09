from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostuplenyForm, RaspredelenyForm
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
    rasp_form = RaspredelenyForm(prefix='rasp')

    if request.method == 'POST':
        post_form = PostuplenyForm(request.POST, prefix='post')
        rasp_form = RaspredelenyForm(request.POST, prefix='rasp')

        if post_form.is_valid() and rasp_form.is_valid():
            post = post_form.save()
            rasp = rasp_form.save(commit=False)
            # если хочешь связать — можно добавить FK позже
            rasp.post = post
            rasp.save()
            return redirect('home')

    return render(request, 'addBook.html', {
        'post_form': post_form,
        'rasp_form': rasp_form
    })

def editBook(request,pk):

    post = get_object_or_404(Postupleny, id=pk)
    rasp = get_object_or_404(Raspredeleny, id=pk)

    if request.method == 'POST':
        form = PostuplenyForm(request.POST, instance=post)
        rasp_form = RaspredelenyForm(request.POST, instance=rasp)

        if form.is_valid() and rasp_form.is_valid():
            form.save()
            rasp_form.save()
            return redirect('home')
    else:
        form = PostuplenyForm(instance=post)
        rasp_form = RaspredelenyForm(instance=rasp)

    return render(request, 'editBooks.html', {
        'form': form,
        'rasp_form': rasp_form
    })
