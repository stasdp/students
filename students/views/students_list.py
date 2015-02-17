# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from ..models.groups import Group
from ..models.students import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from datetime import datetime
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
<<<<<<< HEAD
from django.views.generic import CreateView
=======
>>>>>>> origin/master
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions




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


def students_list(request):
    per_page = 3
    if request.is_ajax():
        order_by = request.GET['order_by']
        try:
            reverse = int(request.GET['reverse'])
        except ValueError:
            reverse = 0
        page = request.GET['page']
        try:
            page = int(page)
        except ValueError:
            page = -1
        if page > 0:
            row_count = int(request.GET['row_count'])+(page - 1) * per_page
        else:
            row_count = int(request.GET['row_count'])
        page = row_count/per_page + 1
        students = Student.objects.all()
        students = students.order_by(order_by)
        if reverse == 1:
            students = students.reverse()
        paginator = Paginator(students, per_page)
        if row_count <= paginator.count:
            students = paginator.page(page)
            html = render_to_string('students/students_list_ajax.html', {'students': students})
            return HttpResponse(html)
        else:
            return HttpResponse(status=204)

    students = Student.objects.all()
    students = students.order_by('last_name')
    if request.GET.get('order_by', '') == '':
        request.GET.order_by = 'last_name'
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, 'students/students_list.html', {'students': students})


# def students_list(request):
#     students = Student.objects.all()

#     # try to order students list

#     order_by = request.GET.get('order_by', '')
#     if order_by in ('last_name', 'first_name', 'ticket', 'id'):
#         students = students.order_by(order_by)
#         if request.GET.get('reverse','') == '1':
#             students = students.reverse()

#     # Paginate_students
#     paginator = Paginator(students, 3)
#     page = request.GET.get("page")
#     try:
#         students = paginator.page(page)
#     except PageNotAnInteger:
#         #if page is not a integer, deliver first page
#         students = paginator.page(1)
#     except EmptyPage:
#         #if page out of range (9999),deliver lasr page of results
#         students = paginator.page(paginator.num_pages)

#     return render(request, 'students/students_list.html',
#         {'students': students})

<<<<<<< HEAD

# def students_add(request):
#     # was form posted?
#     if request.method == "POST":
#         # was form add button clicked?
#         if request.POST.get('add_button') is not None:
#             # errors collection
#             errors = {}

#             # data for student object
#             data = {'middle_name': request.POST.get('middle_name'),
#                     'notes': request.POST.get('notes')}

#             # validate user input
#             first_name = request.POST.get('first_name', '').strip()
#             if not first_name:
#                 errors['first_name'] = u"Имя является обвязательным"
#             else:
#                 data['first_name'] = first_name

#             last_name = request.POST.get('last_name', '').strip()
#             if not last_name:
#                 errors['last_name'] = u"Фамилия является обязательной"
#             else:
#                 data['last_name'] = last_name

#             birthday = request.POST.get('birthday', '').strip()
#             if not birthday:
#                 errors['birthday'] = u"Дата рождения является обязательной"
#             else:
#                 try:
#                     datetime.strptime(birthday, '%Y-%m-%d')
#                 except Exception:
#                     errors['birthday'] = \
#                         u"Введите корректную дату (напр. 1984-12-30)"
#                 else:
#                     data['birthday'] = birthday

#             ticket = request.POST.get('ticket', '').strip()
#             if not ticket:
#                 errors['ticket'] = u"Номер билета является обязательным"
#             else:
#                 data['ticket'] = ticket

#             student_group = request.POST.get('student_group', '').strip()
#             if not student_group:
#                 errors['student_group'] = u"Выберите группу для студента"
#             else:
#                 groups = Group.objects.filter(pk=student_group)
#                 if len(groups) != 1:
#                     errors['student_group'] = u"Выберите конкретную группу"
#                 else:
#                     data['student_group'] = groups[0]


#             photo = request.FILES.get('photo')
#             if photo:
#                 data['photo'] = photo

#             # save student
#             if not errors:
#                 student = Student(**data)
#                 student.save()

#                 # redirect to students list
#                 return HttpResponseRedirect(
#                     u'%s?status_message=Студент успешно добавлен!' %
#                     reverse('home'))
#             else:
#                 # render form with errors and previous user input
#                 return render(request, 'students/students_add.html',
#                     {'groups': Group.objects.all().order_by('title'),
#                      'errors': errors})
#         elif request.POST.get('cancel_button') is not None:
#             # redirect to home page on cancel button
#             return HttpResponseRedirect(
#                 u'%s?status_message=Добавление студета отменено!' %
#                 reverse('home'))
#     else:
#         # initial form render
#         return render(request, 'students/students_add.html',
#             {'groups': Group.objects.all().order_by('title')})


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'ticket', 'student_group', 'notes',]

    def __init__(self, *args, **kwargs):
        super(StudentsAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        #set form tag attr
        self.helper.form_action = reverse('students_add')
        #     kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        #set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        #add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Сохранить',css_class = "btn btn-primary"),
            Submit('cancel_button', u'Отменить', css_class = "btn btn-link"),
        )

class StudentAddView(CreateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentsAddForm

    def get_success_url(self):
        return u'%s?status_message=Студент сохранен!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Создание студента отменено!' \
                % reverse('home'))
        else:
            return super(StudentAddView, self).post(request, *args, **kwargs)

# def students_edit(request, sid):
#     return HttpResponse('<h1>Edit Student %s</h1>' % sid)

# def students_edit(request):
#     # was form posted?
#     if request.method == "POST":
#         # was form add button clicked?
#         if request.POST.get('add_button') is not None:
#             # errors collection
#             errors = {}

#             # data for student object
#             data = {'middle_name': request.POST.get('middle_name'),
#                     'notes': request.POST.get('notes')}

#             # validate user input
#             first_name = request.POST.get('first_name', '').strip()
#             if not first_name:
#                 errors['first_name'] = u"Имя является обвязательным"
#             else:
#                 data['first_name'] = first_name

#             last_name = request.POST.get('last_name', '').strip()
#             if not last_name:
#                 errors['last_name'] = u"Фамилия является обязательной"
#             else:
#                 data['last_name'] = last_name

#             birthday = request.POST.get('birthday', '').strip()
#             if not birthday:
#                 errors['birthday'] = u"Дата рождения является обязательной"
#             else:
#                 try:
#                     datetime.strptime(birthday, '%Y-%m-%d')
#                 except Exception:
#                     errors['birthday'] = \
#                         u"Введите корректную дату (напр. 1984-12-30)"
#                 else:
#                     data['birthday'] = birthday

#             ticket = request.POST.get('ticket', '').strip()
#             if not ticket:
#                 errors['ticket'] = u"Номер билета является обязательным"
#             else:
#                 data['ticket'] = ticket

#             student_group = request.POST.get('student_group', '').strip()
#             if not student_group:
#                 errors['student_group'] = u"Выберите группу для студента"
#             else:
#                 groups = Group.objects.filter(pk=student_group)
#                 if len(groups) != 1:
#                     errors['student_group'] = u"Выберите конкретную группу"
#                 else:
#                     data['student_group'] = groups[0]


#             photo = request.FILES.get('photo')
#             if photo:
#                 data['photo'] = photo

#             # save student
#             if not errors:
#                 student = Student(**data)
#                 student.save()

#                 # redirect to students list
#                 return HttpResponseRedirect(
#                     u'%s?status_message=Студент успешно добавлен!' %
#                     reverse('home'))
#             else:
#                 # render form with errors and previous user input
#                 return render(request, 'students/students_add.html',
#                     {'groups': Group.objects.all().order_by('title'),
#                      'errors': errors})
#         elif request.POST.get('cancel_button') is not None:
#             # redirect to home page on cancel button
#             return HttpResponseRedirect(
#                 u'%s?status_message=Добавление студета отменено!' %
#                 reverse('home'))
#     else:
#         # initial form render
#         return render(request, 'students/students_add.html',
#             {'groups': Group.objects.all().order_by('title')})



class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['first_name', 'last_name',]
        # fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'ticket', 'student_group', 'notes',]


    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        #set form tag attr
        self.helper.form_action = reverse('students_edit',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        #set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        #add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Сохранить',css_class = "btn btn-primary"),
            Submit('cancel_button', u'Отменить', css_class = "btn btn-link"),
        )

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Студент сохранен!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редактирование  студента  отменено!' % reverse('home'))

        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Студент успешно удален!' \
            % reverse('home')

=======
def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}

            # data for student object
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Имя является обвязательным"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Фамилия является обязательной"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата рождения является обязательной"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = \
                        u"Введите корректную дату (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер билета является обязательным"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Выберите группу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Выберите конкретную группу"
                else:
                    data['student_group'] = groups[0]


            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # save student
            if not errors:
                student = Student(**data)
                student.save()

                # redirect to students list
                return HttpResponseRedirect(
                    u'%s?status_message=Студент успешно добавлен!' %
                    reverse('home'))
            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                    {'groups': Group.objects.all().order_by('title'),
                     'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Добавление студета отменено!' %
                reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
            {'groups': Group.objects.all().order_by('title')})


# def students_edit(request, sid):
#     return HttpResponse('<h1>Edit Student %s</h1>' % sid)


class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'ticket', 'student_group', 'notes',]


    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        #set form tag attr
        self.helper.form_action = reverse('students_edit',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        #set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        #add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Сохранить',css_class = "btn btn-primary"),
            Submit('cancel_button', u'Отменить', css_class = "btn btn-link"),
        )

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Студент сохранен!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редактирование студента отменено!' % reverse('home'))

        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Студент успешно удален!' \
            % reverse('home')

>>>>>>> origin/master
# def students_delete(request, sid):
#     return HttpResponse('<h1>Delete Student %s</h1>' % sid)
