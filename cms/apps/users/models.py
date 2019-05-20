# Create your models here.
__author__ = 'cagey'
__date__ = '2019/5/20 1:13 PM'
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    覆盖django中原有的user表
    """
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    # birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # gender = models.CharField(max_length=50, choices=(("male",u"男"),("female","女")),default="female")
    # address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username