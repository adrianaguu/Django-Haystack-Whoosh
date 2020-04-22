from django.shortcuts import render
from .forms import BookForm
from django.shortcuts import redirect

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return render(request,'mesagge.html')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def search(request):
	return render('search/search.html')
