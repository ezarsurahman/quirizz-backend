import uuid
from django.db import models

from quiz.models import Quiz

class Question(models.Model):
    TYPE_CHOICES = {
        "True / False" : "True / False",
        "Multiple Choices" : "Multiple Choices",
        "Short Essay" : "Short Essay"
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name="questions")
    number = models.IntegerField()
    problem = models.TextField()
    type= models.CharField(max_length=255,choices=TYPE_CHOICES)
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"Question {self.number} for {self.quiz.title}"

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
