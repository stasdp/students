# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from ..models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string


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

    # return render(request, 'students/students_list.html',
    #     {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
