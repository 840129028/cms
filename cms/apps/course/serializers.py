__author__ = 'cagey'
__date__ = '2019/5/20 4:25 PM'
from .models import Course, CourseResource, Lesson, Video
from rest_framework import serializers

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseResourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseResource
        fields = "__all__"

class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

