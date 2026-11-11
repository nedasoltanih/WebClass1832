from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView, DetailView, RedirectView, CreateView

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
    template_name = "index.html"

class SuccessView(TemplateView):
    template_name = "success.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context["app_name"] = "Polls"
        return context


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

class NewQuestionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "new_question.html")

    def post(self, request, *args, **kwargs):
        q = Question(
            question_text=request.POST.get("question_text"),
            pub_date=request.PlanguageOST.get("pub_date"),
        )
        q.save()
        return HttpResponse("Thank you for your question.")

class NewQuestionView2(CreateView):
    model = Question
    fields = ["question_text", "pub_date", "language"]
    template_name = "new_question2.html"
    success_url = '/polls/success/'