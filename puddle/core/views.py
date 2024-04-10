from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.all().order_by('-id')[:6] #Get 6 first items not sold
    categories = Category.objects.all() #Get all categories
    #This is done to post and use them in the template
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def login(request):
    return render(request, 'core/login.html')