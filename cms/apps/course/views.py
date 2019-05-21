from django.shortcuts import render

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
from course.serializers import CourseResourceSerializers, CourseSerializers, LessonSerializers, VideoSerializers

from .models import Course, CourseResource, Lesson, Video

class CourseListViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    教程详情数据
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class LessonListViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    章节数据
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers

class VideoListViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    教程视频数据
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

class CourseResourceListViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    教程资源资料数据
    """
    queryset = CourseResource.objects.all()
    serializer_class = CourseResourceSerializers



