from rest_framework import serializers

from questions.serializers import QuestionSerializer
from .models import  Quiz

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)
    class Meta:
        model = Quiz
        fields = ["id","title","description","created_at","category","difficulty","questions"]

