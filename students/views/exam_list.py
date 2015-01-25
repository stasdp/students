# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from ..models.groups import Group
from ..models.students import Student
from ..models.exams import Exam
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string

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

def exam_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')

def exam_edit(request, gid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % gid)

def exam_delete(request, gid):
    return HttpResponse ('<h1> Delete Exam %s</h1>' % gid)
