__author__ = 'cagey'
__date__ = '2019/5/20 1:09 PM'
import xadmin
from .models import Category, Article
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "CMS内容管理系统"
    site_footer = "CMS内容管理系统"
    # menu_style = "accordion"


class CategoryAdmin(object):
    list_display = ["type"]
    list_filter = ["type"]
    search_fields = ['type']

class ArticleAdmin(object):
    list_display = ["title","content","public_time","type","author"]
    list_filter = ["title","type","author","public_time"]
    search_fields = ['title','type','author']
    style_fields = {'content': 'ueditor'}


xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Article,ArticleAdmin)