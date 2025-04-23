from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from myproject.authors.models import Author
from .services import AuthorService
from .dtos import AuthorDTO

class AuthorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, author_id=None):
        if author_id:
            author = AuthorService.get_author(author_id)
            if author:
                return Response(AuthorDTO(author).data)
            return Response({"detail": "Author not found."}, status=status.HTTP_404_NOT_FOUND)
        
        authors = Author.objects.all()
        return Response(AuthorDTO(authors, many=True).data)

    def post(self, request):
        serializer = AuthorDTO(data=request.data)
        if serializer.is_valid():
            author = AuthorService.create_author(serializer.validated_data)
            return Response(AuthorDTO(author).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, author_id):
        author = AuthorService.update_author(author_id, request.data)
        if author:
            return Response(AuthorDTO(author).data)
        return Response({"detail": "Author not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, author_id):
        if AuthorService.delete_author(author_id):
            return Response({"detail": "Author deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Author not found."}, status=status.HTTP_404_NOT_FOUND)