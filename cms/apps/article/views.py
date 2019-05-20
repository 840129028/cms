from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from article.serializers import ArticleSerializers, CategorySerializers
from .models import Category, Article
# from rest_framework_extensions.cache.mixins import CacheResponseMixin


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

    # queryset是一个属性
    # good_viewset.queryset就可以访问到
    # 函数就必须调用good_viewset.get_queryset()函数
    # 如果有了下面的get_queryset。那么上面的这个就不需要了。
    # queryset = Goods.objects.all()

    # throttle_classes = (UserRateThrottle, AnonRateThrottle)
    serializer_class = ArticleSerializers
    pagination_class = ArticlePagination
    queryset = Article.objects.all()

    # 设置列表页的单独auth认证也就是不认证
    # authentication_classes = (TokenAuthentication,)

    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置排序
    # ordering_fields = ('sold_num', 'shop_price')
    # 设置filter的类为我们自定义的类
    # filter_class = ArticleFilter

    # 设置我们的search字段
    search_fields = ('title', 'author','type')


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        文章分类列表数据
    retrieve:
        获取文章分类详情
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
