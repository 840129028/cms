from django.shortcuts import render
import os
from django.views import View
from django.http import HttpResponse
import chardet     # 获取上传文件编码格式
# Create your views here.
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.parsers import JSONParser,MultiPartParser,FileUploadParser
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from users.serializers import Upload_fileSerializer,UserProfileSerializer

from .models import  Upload_file,UserProfile


# Create your views here.
class UserProfileListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    用户信息
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class User_fileListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    用户上传文件信息
    """
    queryset = Upload_file.objects.all()
    serializer_class = Upload_fileSerializer


class Upload_fileListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,viewsets.GenericViewSet):
    '''
    create:
    创建文件
    '''

    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)
    queryset = Upload_file.objects.all()
    serializer_class = Upload_fileSerializer

    parser_classes = (MultiPartParser, FileUploadParser,)
    #
    # def get_permissions(self):
    #     # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    #     permission_classes = [IsAuthenticated]
    #     return [premission() for premission in permission_classes]

class Uploads(View):
   """文件上传 类视图"""
   def get(self, request):
       """表单页面"""
       return render(request, "uploads.html")

   def post(self, request):
       # 获取json文件对象
       obj = request.FILES.get('file_name')
       with open(os.path.join('upload', obj.name), 'wb') as f:
            for line in obj.chunks():
                f.write(line)
       # file_path = os.path.join('upload', obj.name)
       return HttpResponse("上传成功!")
