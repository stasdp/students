# -*- coding: utf-8 -*-
from django.db import models


class Exam(models.Model):
    class Meta(object):
        verbose_name = u'Экзамен'
        verbose_name_plural = u'Экзамены'

    title = models.ForeignKey('Lesson',
        max_length=256,
        blank=False,
        verbose_name=u"Название предмета"
    )

    teacher = models.ForeignKey('Teacher',
        max_length=256,
        blank=False,
        verbose_name=u'Экзаменатор'
    )

    date = models.DateField(
        blank=False,
        verbose_name=u'Дата экзамена',
    )

    exam_group = models.ForeignKey('Group',
        verbose_name = u"Группа",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __unicode__(self):
        return u"%s, %s, %s, %s" % (self.title, self.teacher,self.exam_group ,self.date)
