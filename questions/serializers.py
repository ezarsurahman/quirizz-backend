from questions.models import Choices, Question
from rest_framework import serializers


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ["question","choice_text"]

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True, read_only = True)
    class Meta:
        model = Question
        fields = ["id","quiz","number","type","problem","answer","choices"]
    
