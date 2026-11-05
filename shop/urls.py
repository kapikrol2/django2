from django.urls import path
from . import views
app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.book_add, name="book_add"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
]
