# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def students_list(request):
    students = (
        {'id': 1,
        'first_name': u'Станислав',
        'last_name': u'Панюта',
        'ticket':2223 ,
        'image' : "img/lxllxl.png"},
        {'id': 2,
        'first_name': u'Сергей',
        'last_name': u'Токарь',
        'ticket':2465 ,
        'image' : "img/PB173805.JPG"},
        {'id': 3,
        'first_name': u'Артем',
        'last_name': u'Кучма',
        'ticket':5532 ,
        'image' : "img/фест.jpg"},
        )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
