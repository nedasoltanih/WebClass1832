from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("hi/", views.hi, name="index"),
    path("<int:pk>/",views.QuestionDetailView.as_view(), name="detail"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("login/", views.RedirectQuestionView.as_view(), name="login"),
]