from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AuthorForm, QuoteForm

from .forms import CustomUserCreationForm
from .utils import get_mongo_db




@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Автор успешно добавлен!')
            return redirect('quotes:home')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Цитата успешно добавлена!')
            return redirect('quotes:home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def main(request, page=1):
    db = get_mongo_db()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)

    try:
        quotes_on_page = paginator.page(page)
    except PageNotAnInteger:
        quotes_on_page = paginator.page(1)
    except EmptyPage:
        quotes_on_page = paginator.page(paginator.num_pages)

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered. Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
