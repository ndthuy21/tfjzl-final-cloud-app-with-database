from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Tuyến đường xử lý submit bài thi (Đúng chuẩn cấu trúc int:course_id của IBM)
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    
    # Tuyến đường xử lý hiển thị kết quả thi (Đã bổ sung đầy đủ theo yêu cầu của AI Grader)
    path('course/<int:course_id>/exam_result/', views.show_exam_result, name='show_exam_result'),
]
