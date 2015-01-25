from django.contrib import admin
# from models import Student, Group, Exam, Teacher, Lesson
from models.groups import Group
from models.students import Student
from models.exams import Exam
from models.teachers import Teacher
from models.lessons import Lesson
#



# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
admin.site.register(Teacher)
admin.site.register(Lesson)
