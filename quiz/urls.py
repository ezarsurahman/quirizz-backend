from django.urls import path
from . import views, question_views


urlpatterns = [
    path("", views.QuizListCreate.as_view(), name="quiz-list"),
    path("<uuid:id>/",views.QuizByID.as_view(),name="quiz-by-id"),
    path("<uuid:quizId>/questions/",question_views.CreateListQuestions.as_view(),name="quiz-questions"),
    path("<uuid:quiz_id>/questions/<uuid:id>/", question_views.QuestionByID.as_view(),name="question-by-id")
]