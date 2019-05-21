"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

from article.views import  ArticleListViewSet, CategoryViewset
from course.views import CourseListViewSet,LessonListViewSet,VideoListViewSet,CourseResourceListViewSet
from users.views import Upload_fileListViewSet,UserProfileListViewSet,User_fileListViewSet,Uploads

import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
# from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()

# 配置Article的url
router.register(r'categories', CategoryViewset, base_name="categories")

# 配置Category的url
router.register(r'articles', ArticleListViewSet, base_name="articles")

#配置Course的url
router.register(r'courses',CourseListViewSet,base_name="course")

#配置Lesson的url
router.register(r'lessons',LessonListViewSet,base_name="lesson")

#配置Video的url
router.register(r'videos',VideoListViewSet,base_name="video")

#配置CourseResource的url
router.register(r'courseResources',CourseResourceListViewSet,base_name="courseResource")

#配置Upload_file的url
router.register(r'upload_file',Upload_fileListViewSet,base_name="upload_file")

# #配置User_file的url
router.register(r'user_file',User_fileListViewSet,base_name="user_file")

# #配置UserProfile的url
# router.register(r'userprofile',UserProfileListViewSet,base_name="userprofile")



urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
    # router的path路径
    re_path('^', include(router.urls)),
    # 自动化文档
    path('docs/', include_docs_urls(title='CMS内容管理文档')),
    # 调试登录
    # path('api-auth/', include('rest_framework.urls')),
    # drf自带的token授权登录,获取token需要向该地址post数据
    path('api-token-auth/', views.obtain_auth_token),
    path('upload/',Uploads.as_view()),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
