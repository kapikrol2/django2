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


