from rest_framework import serializers
from .models import Author

class AuthorDTO(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']