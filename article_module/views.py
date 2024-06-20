from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from article_module.models import Article
from article_module.serializers import CreateArticleSerializer, UserSerializer
from .permissions import (IsSuperUser ,IsStaffOrReadOnly, IsAuthorOrReadOnly,IsSuperUserOrStaffReadOnly
)
from rest_framework import viewsets
get_user_model = get_user_model()
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    lookup_field = 'pk'
    filterset_fields = ['title']
    search_fields = ['author','title']
    ordering_fields = ["author"]

    # def get_permissions(self):
    #     if self.action in ['list','create']:
    #         permission_classes = [IsAdminUser]
    #     else:
    #         permission_classes = [IsSuperUserOrStaffReadOnly]
    #     return [permission() for permission in permission_classes]
    #

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model.objects.all()
    serializer_class = UserSerializer


    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsSuperUserOrStaffReadOnly]
        return [permission() for permission in permission_classes]


class ListCreateArticleApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    permission_classes = [IsAdminUser]

class RetrieveUpdateDestroyArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    lookup_field = 'id'
    permission_classes = []


class ListCreateUserApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]

class RetrieveUpdateDestroyUserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CreateArticleApiView(APIView):
    def get(self,request):
        article_object = Article.objects.all()
        serializer = CreateArticleSerializer(article_object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        req_data = request.data
        serializer = CreateArticleSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class UpdateArticleApiView(APIView):
    def put(self,request,id):
        article_object = Article.objects.get(id=id)
        serializer = CreateArticleSerializer(instance=article_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data ,status=status.HTTP_200_OK)
    def delete(self,request,id):
        article_object = Article.objects.get(id = id)
        article_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CreateUserApiView(APIView):
    def get(self,request):
        user_object = get_user_model.objects.all()
        serializer = UserSerializer(user_object,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        req_data = request.data
        serializer = UserSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class UpdateUserApiView(APIView):
    def put(self,request, id):
        user_object = get_user_model.objects.get(id = id)
        req_data = request.data
        serializer = UserSerializer(instance=user_object , data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    def delete(self,request , id):
        user_object = User.objects.get(id = id)
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RevokTokenApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self,request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)