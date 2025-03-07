from django.db import models
import uuid


class Quiz(models.Model):
    CATEGORY_CHOICES = {
        "Trivia": "Trivia",
        "Science": "Science",
        "Social Studies": "Social Studies",
        "English": "English",
        "World Languages": "World Languages",
        "Art": "Art",
        "Culture": "Culture",
        "History": "History",
    }

    DIFFICULTY_CHOICES = {
        "Easy": "Easy",
        "Medium": "Medium",
        "Hard": "Hard",
    }
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255,choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=255,choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    TYPE_CHOICES = {
        "True / False" : "True / False",
        "Multiple Choices" : "Multiple Choices",
        "Short Essay" : "Short Essay"
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    number = models.IntegerField()
    problem = models.TextField()
    type= models.CharField(max_length=255,choices=TYPE_CHOICES)
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"Question {self.number} for {self.quiz.title}"

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

