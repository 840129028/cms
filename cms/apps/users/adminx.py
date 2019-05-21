import xadmin

from xadmin import views  #1,2
from .models import UserProfile,Upload_file

class BaseSetting(object):
    """打开xadmin更换主题功能:1"""
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    """页头,页脚,表收起显示设置:2"""
    site_title = "CMS内容管理系统"
    site_footer = "CMS内容管理系统"
    #左侧列表页折叠样式
    menu_style = "accordion"

xadmin.site.register(views.BaseAdminView,BaseSetting)#1
xadmin.site.register(views.CommAdminView,GlobalSettings)#2

class Upload_fileAdmin(object):
    list_display = ['user', 'file_url']
    search_fields = ['user', 'file_url']
    list_filter = ['user', 'file_url']

# class UserProfileAdmin(object):
#     list_display = ['nick_name', 'gender', 'mobile', 'image']
#     search_fields = ['nick_name', 'gender', 'mobile', 'image']
#     list_filter = ['nick_name', 'gender', 'mobile', 'image']

xadmin.site.register(Upload_file,Upload_fileAdmin)
