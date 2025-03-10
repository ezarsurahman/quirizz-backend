

from django.urls import path

from questions.views import CreateListQuestions, QuestionByID


urlpatterns = [
    path("<uuid:quizId>/",CreateListQuestions.as_view(),name="quiz-questions"),
    path("<uuid:quiz_id>/<uuid:id>/", QuestionByID.as_view(),name="question-by-id")
]