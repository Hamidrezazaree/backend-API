from django.urls import path


from article_module.views import CreateArticleApiView, UpdateArticleApiView, CreateUserApiView, UpdateUserApiView, \
    ListCreateArticleApiView, RetrieveUpdateDestroyArticleDetailAPIView, ListCreateUserApiView, \
    RetrieveUpdateDestroyUserDetailAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('create-article',CreateArticleApiView.as_view(),name= 'create_article'),
    path('update-article/<id>',UpdateArticleApiView.as_view(),name= 'put_article'),
    path('delete-article/<id>',UpdateArticleApiView.as_view(),name= 'delete_article'),
    path('create-user',CreateUserApiView.as_view(),name= 'create_user'),
    path('update-user/<id>',UpdateUserApiView.as_view(),name= 'update_user'),
    path('list-create-article',ListCreateArticleApiView.as_view(),name= 'list-create-article'),
    path('<int:id>',RetrieveUpdateDestroyArticleDetailAPIView.as_view(),name= 'ret_up_des_article'),
    path('list-create-user',ListCreateUserApiView.as_view(),name= 'list_create_user'),
    path('ret/<int:id>',RetrieveUpdateDestroyUserDetailAPIView.as_view(),name= 'ret_user'),
    # path('article/<int:pk>/', ArticleViewSet.as_view({
    #     'get': 'retrieve',
    #     'post': 'create',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy'
    # }), name='article_viewset'),
]
