from rest_framework import serializers

from questions.models import Question
from .models import Submission, SubmissionItem



class SubmissionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubmissionItem
        fields = ['question','answer']

class SubmissionSerializer(serializers.ModelSerializer):
    answers = SubmissionItemSerializer(many=True)
    class Meta:
        model=Submission
        fields = ['quiz','answers','submitted',"grade"]
    
    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        submission, created = Submission.objects.update_or_create(quiz=validated_data["quiz"], defaults={**validated_data})
        submission.grade = 0
        for answer_data in answers_data:
            submission_item, created = SubmissionItem.objects.update_or_create(
                submission=submission, 
                question=answer_data["question"],
                defaults={'answer': answer_data["answer"]}
            )
            question = Question.objects.get(id=answer_data["question"].id)
            if submission_item.answer == question.answer:
                submission.grade += 1
            submission.save()
        return submission
