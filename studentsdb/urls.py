from django.conf.urls import patterns, include, url
from students.views.students_list import StudentList, StudentUpdateView, StudentDeleteView
from students.views.groups_list import GroupDeleteView, GroupAddView, GroupUpdateView
from students.views.exam_list import ExamAddView, ExamUpdateView, ExamDeleteView
from .settings import MEDIA_ROOT, DEBUG


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'students.views.students_list.students_list', name='home'),
    url(r'^students_list$', StudentList.as_view()),
    url(r'^students/add/$', 'students.views.students_list.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',
        StudentUpdateView.as_view(),
        name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),
    # url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students_list.students_delete', name='students_delete'),
    # Groups urls
    url(r'^groups/$', 'students.views.groups_list.groups_list', name='groups'),
    # url(r'^groups/add/$', 'students.views.groups_list.groups_add',name='groups_add'),
    url(r'^groups/add/$', GroupAddView.as_view(),name='groups_add'),
    # url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups_list.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),
    # url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups_list.groups_delete', name='groups_delete'),
    #journal urls
    url(r'^journal/$', 'students.views.journal.journal', name='journal'),
    url(r'^admin/', include(admin.site.urls)),
    #Exam urls
    url(r'^exam/$', 'students.views.exam_list.exam_list', name='exam'),
    url(r'^exam/add/$', ExamAddView.as_view(),name='exam_add'),
    # url(r'^exam/add/$', 'students.views.exam_list.exam_add',name='exam_add'),
    url(r'^exam/(?P<pk>\d+)/edit/$', ExamUpdateView.as_view(), name='exam_edit'),
    # url(r'^exam/(?P<gid>\d+)/edit/$', 'students.views.exam_list.exam_edit', name='exam_edit'),
    url(r'^exam/(?P<gid>\d+)/delete/$', ExamDeleteView.as_view, name='exam_delete'),
    # url(r'^exam/(?P<gid>\d+)/delete/$', 'students.views.exam_list.exam_delete', name='exam_delete'),
    #Contact admin form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),
    #testing contact_form
    url(r'^contact/$', 'students.views.contact_admin.contact_admin', name='contact_form'),

)
if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{
            'document_root':MEDIA_ROOT}))
