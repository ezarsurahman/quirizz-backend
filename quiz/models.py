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
