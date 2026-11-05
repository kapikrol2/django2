from django.http import Http404
from django.shortcuts import redirect, render
from .forms import BookForm, SearchForm

BOOKS = [
    {"id": 1, "title": "Wiedźmin", "author": "Andrzej Sapkowski", "price": 49.99, "in_stock": True},
    {"id": 2, "title": "Diuna", "author": "Frank Herbert", "price": 59.90, "in_stock": False},
    {"id": 3, "title": "Hobbit", "author": "J.R.R. Tolkien", "price": 39.50, "in_stock": True},
    {"id": 4, "title": "Rok 1984", "author": "George Orwell", "price": 29.99, "in_stock": False},
    {"id": 5, "title": "Problem trzech ciał", "author": "Cixin Liu", "price": 45.00, "in_stock": True},
]


def index(request):
    return render(request, "shop/index.html")


def book_list(request):
    form = SearchForm(request.GET)
    books = BOOKS

    if form.is_valid():
        q = form.cleaned_data.get("q")
        in_stock_only = form.cleaned_data.get("in_stock_only")

        if q:
            books = [b for b in books if q.lower() in b["title"].lower() or q.lower() in b["author"].lower()]
        if in_stock_only:
            books = [b for b in books if b["in_stock"]]

    return render(request, "shop/book_list.html", {"books": books, "form": form})


def book_detail(request, book_id):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if book is None:
        raise Http404("Nie znaleziono książki")
    return render(request, "shop/book_detail.html", {"book": book})


