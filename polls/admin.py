from django.contrib import admin

# Register your models here.

from . models import Question
# 在登录admin之后，就可以对Question进行增删改查
admin.site.register(Question)