# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..models.groups import Group
from ..models.students import Student
from ..models.exams import Exam
from ..models.teachers import Teacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.template.loader import render_to_string
from django.views.generic import DeleteView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from datetime import datetime



def exam_list(request):
    exams = Exam.objects.all()

    # try to order exam list

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'date', 'teacher','exam_group' ):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            exams = exams.reverse()

    # Paginate_exams
    paginator = Paginator(exams, 3)
    page = request.GET.get("page")
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        #if page is not a integer, deliver first page
        exams = paginator.page(1)
    except EmptyPage:
        #if page out of range (9999),deliver lasr page of results
        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exam_list.html',
        {'exams': exams })

# def exam_add(request):
#     return HttpResponse('<h1>Exam Add Form</h1>')

# def exam_edit(request, gid):
#     return HttpResponse('<h1>Edit Exam %s</h1>' % gid)

# def exam_delete(request, gid):
#     return HttpResponse ('<h1> Delete Exam %s</h1>' % gid)

class ExamAddForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        # fields = ['lessons', 'teacher', 'date', 'group']

    def __init__(self, *args, **kwargs):
        super(ExamAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        #set form tag attr
        self.helper.form_action = reverse('groups_add')
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

class ExamAddView(CreateView):
    model = Exam
    template_name = 'students/exam_add.html'
    form_class = ExamAddForm

    def get_success_url(self):
        return u'%s?status_message=Экзамен сохранен!' % reverse('exam')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Создание экзамена отменено!' % reverse('exam'))
        else:
            return super(ExamAddView, self).post(request, *args, **kwargs)

class ExamUpdateForm(ModelForm):
    class Meta:
        model = Exam
        # fields = ['title', 'leader', 'notes']


    def __init__(self, *args, **kwargs):
        super(ExamUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        #set form tag attr
        self.helper.form_action = reverse('exam_edit',
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

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'students/exam_edit.html'
    form_class = ExamUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Экзамен сохранен!' % reverse('exam')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редактирование экзамена отменено!' % reverse('exam'))

        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'students/exam_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Экзамен успешно удален!' \
            % reverse('exam')
