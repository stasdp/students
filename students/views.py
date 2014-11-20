# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# #Students views
# def students_journal(request):
#     return HttpResponse ('<h2> Student journal </h2>')

# def student_test(request):
#     return HttpResponse('<h2>Hello Kitty</h2>')

# def students_list(request):
#     return render(request, 'students/students_list.html', {})

# def students_add(request):
#     return HttpResponse('<h1>Student Add Form</h1>')

# def students_edit(request, sid):
#     return HttpResponse('<h1>Edit Student %s</h1>' % sid)

# def students_delete(request, sid):
#     return HttpResponse('<h1> Delete student %s</h1>' % sid)

# #groups views

# def groups_list(request):
#     return HttpResponse('<h1>Groups listing</h1>')

# def groups_add(request):
#     return HttpResponse('<h1>Group Add Form</h1>')

# def groups_edit(request, gid):
#     return HttpResponse('<h1>Edit Group %s</h1>' % gid)



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

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
        'name' : '6-TM',
        'starosta' : {'id':1, 'name' : u'Панюта Станислав'}},
        {'id': 2,
        'name' : '6-TK',
        'starosta' : {'id' : 2, 'name' :u'Токарь Сергей'}},
        {'id': 3,
        'name' : '6-TP',
        'starosta' : {'id' : 3, 'name' :u'Кучма Артем'}},
        )

    return render(request, 'students/groups_list.html', {'groups' : groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse ('<h1> Delete Group %s</h1>' % gid)