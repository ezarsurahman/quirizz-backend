import django_filters

from quiz.models import Quiz


class QuizFilter(django_filters.FilterSet):
    class Meta:
        model = Quiz
        fields = {
            'title' : ["exact", "contains"],
            'description' : ["exact","contains"],
            'category' : ["exact"],
            'created_at' : ["exact","range"]
        }