from rest_framework import serializers
from article_module.models import Article
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','email','first_name','last_name']


class CreateArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = ['title','author']

    def validate_title(self, value):
        filter_list = ["java", "cython", "js"]
        for item in filter_list:
            if item in value:
                raise serializers.ValidationError("sorry you use bad word")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

