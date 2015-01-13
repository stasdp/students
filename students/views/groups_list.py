# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from ..models import Group
from ..models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string


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

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse ('<h1> Delete Group %s</h1>' % gid)
