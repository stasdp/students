# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..models.groups import Group
from ..models.students import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.views.generic import DeleteView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from datetime import datetime

# def groups_list(request):
#     per_page = 3
#     if request.is_ajax():
#         order_by = request.GET['order_by']
#         try:
#             reverse = int(request.GET['reverse'])
#         except ValueError:
#             reverse = 0
#         page = request.GET['page']
#         try:
#             page = int(page)
#         except ValueError:
#             page = -1
#         if page > 0:
#             row_count = int(request.GET['row_count'])+(page - 1) * per_page
#         else:
#             row_count = int(request.GET['row_count'])
#         page = row_count/per_page + 1
#         groups = Group.objects.all()
#         groups = groups.order_by(order_by)
#         if reverse == 1:
#             groups = groups.reverse()
#         paginator = Paginator(groups, per_page)
#         if row_count <= paginator.count:
#             groups = paginator.page(page)
#             html = render_to_string('students/groups_list.html', {'groups': groups})
#             return HttpResponse(html)
#         else:
#             return HttpResponse(status=204)

#     groups = Group.objects.all()
#     groups = groups.order_by('title')
#     if request.GET.get('order_by', '') == '':
#         request.GET.order_by = 'title'
#     order_by = request.GET.get('order_by', '')
#     if order_by in ('title', 'leader', ):
#         groups = groups.order_by(order_by)
#         if request.GET.get('reverse', '') == '1':
#             groups = groups.reverse()
#     paginator = Paginator(groups, 3)
#     page = request.GET.get('page')
#     try:
#         groups = paginator.page(page)
#     except PageNotAnInteger:
#         groups = paginator.page(1)
#     except EmptyPage:
#         groups = paginator.page(paginator.num_pages)
#     return render(request, 'students/groups_list.html', {'groups': groups})

def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'id', ):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            groups = groups.reverse()

    # Paginate_groups
    paginator = Paginator(groups, 3)
    page = request.GET.get("page")
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        #if page is not a integer, deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        #if page out of range (9999),deliver lasr page of results
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html',
        {'groups': groups})

# def groups_add(request):
#     return HttpResponse('<h1>Group Add Form</h1>')

class GroupAddForm(ModelForm):
    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(GroupAddForm, self).__init__(*args, **kwargs)

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

class GroupAddView(CreateView):
    model = Group
    template_name = 'students/groups_add.html'
    form_class = GroupAddForm

    def get_success_url(self):
        return u'%s?status_message=Группа сохранена!' % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Создание группы отменено!' % reverse('groups'))
        else:
            return super(GroupAddView, self).post(request, *args, **kwargs)


# def groups_edit(request, gid):
#     return HttpResponse('<h1>Edit Group %s</h1>' % gid)

class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        # fields = '__all__'
        # fields = ['title', 'leader', 'notes']


    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        #set form tag attr
        self.helper.form_action = reverse('groups_edit',
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

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Группа сохранена!' % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редактирование группы отменено!' % reverse('groups'))

        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


# def groups_delete(request, gid):
#     return HttpResponse ('<h1> Delete Group %s</h1>' % gid)

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Группа успешно удалена!' \
            % reverse('home')
