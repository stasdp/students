# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from ..models import Group
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

#     return render(request, 'students/students_list.html',
#         {'students': students})

def students_add(request):
    if request.method == "POST":
        if request.POST.get('add_button') is not None:
            # TODO: validate input from user

            errors = {}

            if not errors:
                #создаем обьект студента
                student = Student(
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    middle_name = request.POST['middle_name'],
                    birthday = request.POST['birthday'],
                    ticket = request.POST['ticket'],
                    student_group = Group.objects.get(pk=request.POST['student_group']),
                    photo = request.FILES['photo'],
                )
                student.save()

                return HttpResponseRedirect(reverse('home'))

            else:
                return render(request,'students/students_add.html',
                    {'groups': Group.objects.all().order_by('title'),
                    'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            #вернуть домой при нажатии на эту кнопку
            return HttpResponseRedirect(reverse('home'))

    else:

        return render(request, 'students/students_add.html',{'groups': Group.objects.all().order_by('title')})

    # Якщо форма була запощена:

        # Якщо кнопка Скасувати була натиснута:
            # Повертаємо користувача до списку студентів
    # Якщо кнопка Додати була натиснута:
        # Перевіряємо дані на коректність та збираємо помилки
            # Якщо дані були введені некоректно:
                # Віддаємо шаблон форми разом із знайденими помилками
            # Якщо дані були введені коректно:
                # Створюємо та зберігаємо студента в базу
                    # Повертаємо користувача до списку студентів
    # Якщо форма не була запощена:
        # повертаємо код початкового стану форми

    return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
