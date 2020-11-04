"""MyDjango3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path,include
from MyDjango3 import views
from django.contrib import admin

urlpatterns = [
    # path('hello/', views.hello),
    path('runoob/', views.runoob),

#     这个 include() 函数允许引用其他urlconfs。每当Django遇到 include() ，它会切掉与该点匹配的URL的任何部分，并将剩余的字符串发送到包含的urlconf以进行进一步处理。
    path('polls/', include('polls.urls')),
    path('admin/',admin.site.urls),
]