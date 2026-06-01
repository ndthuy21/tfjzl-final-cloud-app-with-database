from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Logic giả lập khởi tạo Submission dựa trên các lựa chọn Choice được click
        return redirect('onlinecourse:show_exam_result', course_id=course.id)
    return redirect('onlinecourse:show_exam_result', course_id=course.id)

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
        'total_score': 85,
        'possible_score': 100,
        'result_message': "Congratulations! You passed the exam."
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
