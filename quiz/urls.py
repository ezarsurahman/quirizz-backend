from django.urls import path

from . import views

from submission.views import SubmissionListCreate


urlpatterns = [
    path("", views.QuizListCreate.as_view(), name="quiz-list"),
    path("<uuid:id>/",views.QuizByID.as_view(),name="quiz-by-id"),
    path("<uuid:quiz_id>/submit/",SubmissionListCreate.as_view(),name="quiz-submit"),
]