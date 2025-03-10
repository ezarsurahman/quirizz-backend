from django.db import models

from questions.models import Question
from quiz.models import Quiz

class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submission')
    submitted = models.BooleanField()
    grade = models.IntegerField()

    # @property
    # def grade(self):
    #     grade = 0
    #     answers = SubmissionItem.objects.filter(submission=self)
    #     questions = Question.objects.filter(quiz=self.quiz)
    #     total_question = len(questions)
    #     for answer in answers:
    #         question = Question.objects.get(question=question)
    #         if answer.answer == question.answer:
    #             grade += 1
    #     return f"{grade}/{total_question}"



class SubmissionItem(models.Model):
    submission = models.ForeignKey(Submission, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(blank=True)
