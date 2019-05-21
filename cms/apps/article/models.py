from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.


class Category(models.Model):
    """
    文章种类
    """
    type = models.CharField(max_length=20,verbose_name="文章种类")

    class Meta:
        verbose_name = '文章种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type



class Article(models.Model):
    """
    文章信息
    """
    title = models.CharField(max_length=20,verbose_name="文章标题")
    # content = models.TextField(verbose_name="文章内容")
    content = UEditorField(verbose_name=u"文章内容", imagePath="article/images/", width=1000, height=300,
                              filePath="article/files/", default='')
    public_time = models.TimeField(default=datetime.now,verbose_name="发布时间")
    type = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="文章种类")
    # lmsg = models.ManyToManyField(Lmsg, blank=True,verbose_name="文章留言")
    author = models.CharField(max_length=10,blank=True,verbose_name="文章作者")

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title