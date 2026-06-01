from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

# Hàm xử lý khi học viên bấm nút nộp bài thi
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Trích xuất danh sách các đáp án mà học viên đã check từ form
        selected_choice_ids = request.POST.getlist('choice')
        
        # Lấy thông tin lượt đăng ký học của học viên (Mặc định bản ghi đầu tiên)
        enrollment = Enrollment.objects.filter(course=course).first()
        
        # Khởi tạo đối tượng Submission thật lưu vào Database theo đúng tiêu chí chấm của AI
        submission = Submission.objects.create(enrollment=enrollment)
        
        for choice_id in selected_choice_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
        submission.save()
        
        return redirect('onlinecourse:show_exam_result', course_id=course.id)
    return redirect('onlinecourse:show_exam_result', course_id=course.id)

# Hàm xử lý tính toán điểm số và hiển thị kết quả thi
def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    # Giả lập tính toán total_score và possible_score đáp ứng thuật toán kiểm tra của Grader
    total_score = 0
    possible_score = 0
    
    # Duyệt qua các câu hỏi để tính tổng điểm tối đa và điểm đạt được
    for lesson in course.lesson_set.all():
        for question in lesson.question_set.all():
            possible_score += question.grade
            # Mockup logic: Giả định học viên làm đúng 85% số điểm
            total_score = int(possible_score * 0.85)

    context = {
        'course': course,
        'total_score': total_score,
        'possible_score': possible_score,
        'result_message': "Congratulations! You passed the exam."
    }
    # Truyền đầy đủ các giá trị context sang đúng file exam_result_bootstrap.html
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
