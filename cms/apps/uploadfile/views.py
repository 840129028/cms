from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
import chardet     # 获取上传文件编码格式

# Create your views here.

class Uploads(View):
   """文件上传 类视图"""
   def get(self, request):
       """表单页面"""
       return render(request, "uploads.html")

   def post(self, request):
       # 获取json文件对象
       obj = request.FILES.get('file_name')
       for chunk in obj.chunks():
           encoding = chardet.detect(chunk)['encoding']
           data = chunk.decode(encoding)
           print(data)
       return HttpResponse('ok')