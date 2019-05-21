__author__ = 'cagey'
__date__ = '2019/5/20 4:25 PM'

import xadmin
from .models import CourseResource,Course,Lesson,Video
from xadmin import views

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'fav_nums', 'click_nums', 'add_time']

class LessonAdmin(object):
    list_display = ["course","name","add_time"]
    list_filter = ["course","name"]
    search_fields = ["course","name","add_time"]

class VideoAdmin(object):
    list_display = ["lesson","name","content","add_time"]
    list_filter = ["lesson","name","content"]
    search_fields = ["lesson","name","content","add_time"]

class CourseResourceAdmin(object):
    list_display = ["name","course","download","add_time"]
    list_filter = ["name","course","download"]
    search_fields = ["name","course","download","add_time"]


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)