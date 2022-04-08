from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post,Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =['id','username']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only = True)
    class Meta:
        model= Post
        fields ="__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['message','author']


#author
# id
# username
#
#