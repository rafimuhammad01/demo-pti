from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer
from rest_framework import status

# Create your views here.

class BookList(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializers = BookSerializer(book, many=True)
        return Response(serializers.data)

    def post(self, request):
        book = Book.objects.create(
            name = request.data['name'],
            author = request.data['author'],
            volume = request.data['volume'],
            total_page = request.data['total_page'],
            publisher = request.data['publisher'],
            published_date = request.data['published_date'],
        )

        serializers = BookDetailSerializer(book)
        return Response(serializers.data, status=status.HTTP_201_CREATED)



class BookDetail(APIView):
    def get(self, request, id):
        try :
            book = Book.objects.get(id=id)
            serializers = BookDetailSerializer(book)
        except Book.DoesNotExist :
            return Response({
                "error" : "buku tidak ditemukan"
            })
        return Response({
            "status" : 200,
            "message" : "get book success",
            "data" : serializers.data
        })

    def put(self, request, id):
        try :
            book = Book.objects.get(id=id)
            book.name = request.data['name']
            book.author = request.data['author']
            book.volume = request.data['volume']
            book.total_page = request.data['total_page']
            book.publisher = request.data['publisher']
            book.published_date = request.data['published_date']
            book.save()
        except Book.DoesNotExist:
             return Response({
                "error" : "buku tidak ditemukan"
            })

        serializers = BookDetailSerializer(book)
        return Response({
            "status" : 201,
            "message" : "update successfull",
            "data" : serializers.data
        }, status=status.HTTP_201_CREATED)


    def delete(self, request, id) :
        book = Book.objects.get(id=id)
        book.delete()

        return Response({
            "status" : 201,
            "message" : "delete success",
        }, status=status.HTTP_201_CREATED)

        