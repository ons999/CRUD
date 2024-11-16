from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    # GET request - List all books
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # POST request - Add a new book
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET request - Retrieve a specific book
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # PUT request - Update a specific book
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,{'Created':'Thanks God'}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request - Delete a specific book
    elif request.method == 'DELETE':
        book.delete()
        return Response({'error':'Item was Deleted'},status=status.HTTP_204_NO_CONTENT)
