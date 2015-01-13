# -*- coding: utf-8 -*-
from django.db import models

class Student(models.Model):
    class Meta(object):
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенты'

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Имя')

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Фамилия')

    middle_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Отчество')

    birthday = models.DateField(
        blank=False,
        verbose_name=u'Дата рождения',
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name=u'Фото',
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Билет')

    notes = models.TextField(
        blank=True,
        verbose_name=u'Дополнительные ведомости')

    student_group = models.ForeignKey('Group',
        verbose_name=u'Группа',
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Группы"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Название группы")

    leader = models.OneToOneField('Student',
        verbose_name=u"Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Дополнительные ведомости")

    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name,
                 self.leader.last_name)
        else:
            return u"%s" % (self.title,)

class Teacher(models.Model):
    class Meta(object):
        verbose_name = u'Преподаватель'
        verbose_name_plural = u'Преподаватели'

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Имя')

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Фамилия')

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Lesson(models.Model):
    class Meta(object):
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Название предмета'
    )
    def __unicode__(self):
        return "%s " % self.title

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
