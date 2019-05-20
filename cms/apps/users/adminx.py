import xadmin
# from .models import EmailVerifycord,Banner
from xadmin import views  #1,2

class BaseSetting(object):
    """打开xadmin更换主题功能:1"""
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    """页头,页脚,表收起显示设置:2"""
    site_title = "CMS内容管理系统"
    site_footer = "CMS内容管理系统"
    menu_style = "accordion"

xadmin.site.register(views.BaseAdminView,BaseSetting)#1
xadmin.site.register(views.CommAdminView,GlobalSettings)#2