from django.shortcuts import render, get_object_or_放置_404, redirect
from .models import Course, Lesson, Question, Choice, Submission

def submit(request, course_id):
    context = {}
    return redirect('onlinecourse:show_exam_result', course_id=course_id)

def show_exam_result(request, course_id):
    context = {}
    return render(request, 'onlinecourse/exam_result.html', context)
