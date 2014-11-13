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

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

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

# def groups_delete(request, gid):
#     return HttpResponse ('<h1> Delete Group %s</h1>' % gid)

def students_list(request):
    return render(request, 'students/students_list.html', {})

# def students_add(request):
#     return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
