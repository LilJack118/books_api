from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=400)
    authors = serializers.ListField(required = False, allow_null = True)
    publishedDate = serializers.CharField(max_length=10, required = False, allow_null = True)
    categories = serializers.ListField(required = False, allow_null = True)
    average_rating = serializers.FloatField(required = False, allow_null = True)
    ratings_count = serializers.FloatField(required = False, allow_null = True)
    thumbnail = serializers.URLField(required = False, allow_null = True)

    # condition for create 
    def create(self, validated_data):
        # The ** operator allows us to take a dictionary of key-value pairs and 
        # unpack it into keyword arguments in a function call
        return Book.objects.update_or_create(**validated_data)
