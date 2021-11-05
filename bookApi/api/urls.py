from django.urls import path, re_path
from . import views

urlpatterns = [
    path('books', views.BookList.as_view(), name='BookList'),
    path('books/<pk>', views.SingleBook.as_view(), name='SingleBook'),
    path('db', views.PostNewBooks.as_view(), name='db'),
    path('dbHobbit', views.PostHobbitBooks.as_view(), name='PostHobbitBooks'),
]
