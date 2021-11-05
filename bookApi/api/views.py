from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status #this allows to display custome status code
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from . import flat_dicts_json

import requests

# Create your views here.


class BookList(ListAPIView):

    model = Book
    serializer_class = BookSerializer

    # define function on get request
    def get_queryset(self):

        publishedDate = self.request.query_params.get('published_date')
        author = self.request.query_params.get('author')
        sort = self.request.query_params.get('sort')
        queryset =  Book.objects.all()

        if author:
            queryset = queryset.filter(authors__icontains=author)

        if publishedDate:

            queryset = queryset.filter(publishedDate__contains=publishedDate)

        if sort:
            order_sign = '-' if sort == '-published_date' else '' 
            queryset = queryset.order_by(order_sign + 'publishedDate')

        return queryset

        

class PostNewBooks(APIView):
    def post(self, request):

        url='https://www.googleapis.com/books/v1/volumes?q=war'
        response = requests.get(url=url)
        data = response.json()['items']


        if type(data) == list:
            processed_data = flat_dicts_json.flatten_dictionaries_list(data)
            serializer = BookSerializer(data=processed_data, many=True)
        else:
            processed_data = flat_dicts_json.flatten_dictionary(data, {})
            serializer = BookSerializer(data=processed_data)
            

        if serializer.is_valid():

            serializer.save()
            
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PostHobbitBooks(APIView):
    def post(self, request):

        url='https://www.googleapis.com/books/v1/volumes?q=Hobbit'
        response = requests.get(url=url)
        data = response.json()['items']


        if type(data) == list:
            processed_data = flat_dicts_json.flatten_dictionaries_list(data)
            serializer = BookSerializer(data=processed_data, many=True)
        else:
            processed_data = flat_dicts_json.flatten_dictionary(data, {})
            serializer = BookSerializer(data=processed_data)
            

        if serializer.is_valid():

            serializer.save()
            
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class SingleBook(APIView):

    def get(self, request, pk):
        try:
            movie = Book.objects.get(id=pk)
        except:#if book not found
            return Response({"Error": 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(movie)
        return Response(serializer.data)

