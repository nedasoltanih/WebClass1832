from django.http import HttpResponse, Http404
from django.template import loader
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView, DetailView, RedirectView

from polls.models import Question

def index(request):
    questions = Question.objects.all()
    # output = ", ".join([q.question_text for q in questions])
    # return HttpResponse(output)
    template = loader.get_template("index.html")
    context = {"latest_question_list": questions}
    return HttpResponse(template.render(context, request))

class IndexView(ListView):
    model = Question
    context_object_name = "questions"

class SuccessView(TemplateView):
    template_name = "success.html"



# @require_http_methods(["GET"])
# def detail(request, q_id):
#     try:
#         q = Question.objects.get(pk=q_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     # return HttpResponse(q.question_text + ", Published at:" + str(q.pub_date))
#     template = loader.get_template("detail.html")
#     context = {"question": q}
#     return HttpResponse(template.render(context, request))

class QuestionDetailView(DetailView):
    model = Question

class RedirectQuestionView(RedirectView):
    permanent = True
    pattern_name = 'success'

def test_view(request):
    return HttpResponse("hello")