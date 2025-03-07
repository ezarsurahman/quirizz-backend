from rest_framework import serializers
from .models import Choices, Question, Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id","title","description","created_at","category","difficulty"]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id","quiz","number","type","problem","answer"]

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ["question","choice_text"]