from django.views.generic import ListView
from student.models.students import Student

class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template = 'students/student_list'

    def get_context_data(self, **kwargs):
        #get original context data from parent class
        context = super(StudentList, self).get_context_data(**kwargs)

        #tell template no to show logo on a page
        context['show_logo'] = False

        #return context maping
        return context

    def get_queryset(self):
        #get original query set
        qs = super(StudentList, self).get_queryset()

        #order by last name
        return qs.order_by('last_name')
