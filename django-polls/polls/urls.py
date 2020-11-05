from django.urls import path
from.import views

# Django如何区分URL名称？例如， polls 应用程序有一个 detail 在同一个项目上的应用程序，也可能是用于博客的应用程序。如何使Django知道在使用 {{%url%}} 模板标签？
# 答案是向URLConf添加名称空间。在 polls/urls.py 文件，继续添加 app_name 要设置应用程序命名空间：
app_name = 'polls'

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('index2/', views.index2, name='index2'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),


]
'''

'''

'''
# ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # question_id 与detail方法中的question_id 对应
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('index',views.index,name='index'),
    # path('/vote/',views.vote,name='vote'),
'''