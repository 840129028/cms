from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from article.serializers import ArticleSerializers, CategorySerializers
from .models import Category, Article



class ArticlePagination(PageNumberPagination):
    """
    文章列表分页类
    """
    page_size = 12
    # 向后台要多少条
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100

class ArticleListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    文章列表页，分页，搜索，过滤，排序,取某一篇文章的详情
    """

    # throttle_classes = (UserRateThrottle, AnonRateThrottle)
    serializer_class = ArticleSerializers
    pagination_class = ArticlePagination
    queryset = Article.objects.all()

    # 设置列表页的单独auth认证也就是不认证
    # authentication_classes = (TokenAuthentication,)

    # 设置三大常用过滤器DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 设置search字段
    search_fields = ('title', 'author','type')


class CategoryViewset(mixins.CreateModelMixin,mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        文章分类列表数据
    retrieve:
        获取文章分类详情
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
