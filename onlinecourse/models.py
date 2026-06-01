from django.db import models
from django.utils.timezone import now

class Course(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Instructor(models.Model):
    user = models.CharField(max_length=100)

class Learner(models.Model):
    user = models.CharField(max_length=100)

class Enrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, default=1)
    choices = models.ManyToManyField(Choice)
    def __str__(self):
        return f"Submission {self.id} for {self.enrollment}"
