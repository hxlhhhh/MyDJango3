from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from django.http import Http404
from .models import Question,Choice
from django.views import generic
#  1 response 返回
'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))
'''
# 2 render渲染方式
def index(request):
    print("222222222222222")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # 按照惯例 DjangoTemplates 在每个目录中查找"templates"子目录 查找poll/index.html
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    print("66666666666666666666666666")
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    print("7777777777777777777777")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
def vote(request, question_id):
    print("88888888888888888888888888")
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    try:
        # 根据名字获取value值
        # print(request.POST['choice'])
        # 根据主键查询
        # question.choice_set.get(pk=request.POST['choice'])
        # 查询所有
        # print(question.choice_set.all())
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        # 保存到数据库
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # args 是将question.id赋值给了path('<int:question_id>/results/', views.results, name='results'),中的question_id

        # reverse('polls:results' 防止硬编码的形式
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def index2(request):
    return render(request, 'polls/index2.html',)




class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

#  ListView 和 DetailView . 这两个视图分别抽象了“显示对象列表”和“显示特定类型对象的详细信息页”的概念。
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'




