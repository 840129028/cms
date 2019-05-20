__author__ = 'cagey'
__date__ = '2019/5/20 1:36 PM'

from .models import Category, Article
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
#
# class LmsgSerializaers(serializers.ModelSerializer):
#     class Meta:
#         model = Lmsg
#         fields = "__all__"