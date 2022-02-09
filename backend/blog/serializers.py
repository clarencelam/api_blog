from rest_framework import serializers
from .models import BlogPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostSerializer
        fields = '__all__'
        lookup_field = 'slug'