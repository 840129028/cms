from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"教程名")
    desc = models.CharField(max_length=300, verbose_name=u"教程描述")
    detail = models.TextField(verbose_name=u"教程详情")
    # degree = models.CharField(choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=20, verbose_name=u"难度")
    # learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    # students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/image/%Y/%m", max_length=100, verbose_name=u"上传图片")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"教程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"教程", on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name=u"章节名字")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名字")
    content = models.FileField(upload_to="course/vedio/", null=True, blank=True, verbose_name="视频内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"教程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"教程资源"
        verbose_name_plural = verbose_name
















