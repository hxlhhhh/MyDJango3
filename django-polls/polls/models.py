
# Create your models here.

from django.db import models
from datetime import timezone
import datetime
from django.utils import timezone
# 每个模型都由一个子类表示 django.db.models.Model .每个模型都有许多类变量，每个变量表示模型中的数据库字段。
class Question(models.Model):
    # 每个字段都由 Field 类，例如， CharField 用于字符字段和 DateTimeField 日期时间。这将告诉Django每个字段包含的数据类型。
    # 一些 Field 类具有必需的参数。 CharField 例如，要求给它一个 max_length . 这不仅在数据库模式中使用，而且在验证中使用
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
    # 最后，注意定义了一个关系，使用 ForeignKey . 告诉 Django 每个人 Choice 与单个 Question . Django支持所有常见的数据库关系：多对一、多对多和一对一。
    # ,related_name="zhangsa"前端对应
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    # A Field 也可以有各种可选参数；在本例中，我们已经设置了 default 价值 votes 到0。
    votes=models.IntegerField(default=0)
    # 返回对象时，以什么样的格式返回
    def __str__(self):
        return self.choice_text