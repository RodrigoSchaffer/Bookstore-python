from .models import Author
from .dtos import AuthorDTO

class AuthorService:

    @staticmethod
    def get_author(author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def create_author(data):
        author = Author.objects.create(name=data['name'])
        return author

    @staticmethod
    def update_author(author_id, data):
        author = Author.objects.filter(id=author_id).first()
        if author:
            author.name = data.get('name', author.name)
            author.save()
            return author
        return None

    @staticmethod
    def delete_author(author_id):
        author = Author.objects.filter(id=author_id).first()
        if author:
            author.delete()
            return True
        return False