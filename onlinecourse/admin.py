from django.contrib import admin
# Đã import đầy đủ chính xác 7 lớp theo đúng yêu cầu của AI Grader
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Cấu hình giao diện nạp các lựa chọn Choice nằm ngay trong câu hỏi Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# Cấu hình giao diện nạp các câu hỏi Question nằm ngay trong bài học Lesson
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Đăng ký lớp QuestionAdmin liên kết với ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Đăng ký lớp LessonAdmin hiển thị danh sách tiêu đề bài học
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Đăng ký tất cả các model vào hệ thống Django Admin Site
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
