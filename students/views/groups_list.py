# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

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
