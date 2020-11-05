from django.contrib import admin

# Register your models here.

from . models import Question,Choice
# admin.StackedInline 竖着
# admin.TabularInline 横着
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
# 自定义管理窗体
class QuestionAdmin(admin.ModelAdmin):
    # 添加时展示的设置
    # “发布日期”位于“问题”字段之前：
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # 展示时显示几个
    list_display = ('question_text', 'pub_date','was_published_recently')
    # 设置关联的外键展示
    inlines = [ChoiceInline]
    # 根据pub_date 添加筛选功能 显示的过滤器类型取决于要过滤的字段类型。因为 pub_date 是一个 DateTimeField Django知道给出适当的过滤选项：“任意日期”、“今天”、“过去7天”、“本月”、“今年”。
    list_filter = ['pub_date']
    # 添加搜索
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# 在登录admin之后，就可以对Question进行增删改查
admin.site.register(Choice)