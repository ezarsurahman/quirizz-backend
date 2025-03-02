from django.urls import path
from . import views

urlpatterns = [
    path("", views.QuizListCreate.as_view(), name="quiz-list"),
    path("delete/<uuid:id>/",views.QuizDelete.as_view(),name="quiz-delete"),
    path("update/<uuid:id>/",views.QuizUpdate.as_view(),name="quiz-update"),
    path("<uuid:id>/",views.QuizByID.as_view(),name="quiz-by-id"),
]