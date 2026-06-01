from django.db import models
from django.utils.timezone import now

class Course(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(max_length=500)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_shared=True, on_delete=models.CASCADE)

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    choices = models.ManyToManyField(Choice)
