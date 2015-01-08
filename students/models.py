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

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

# class Group(models.Model):
#     class Meta(object):
#         verbose_name=u'Группа'
#         verbose_name_plural=u'Группы'

#     title = models.CharField(
#         max_length=256,
#         blank=False,
#         verbose_name=u'Название группы')

#     leader = models.OneToOneField('Student',
#         verbose_name=u'Староста',
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL)

#     notes = models.TextField(
#         blank=True,
#         verbose_name=u'Дополнительные ведомости')

#     def __unicode__(self):
#         if self.leader:
#             return u"%s (%s %s)" % (self.title, self.leader.first_name,self.leader.last_name)
#         else:
#             return u"%s" % (self.title,)


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



    # def __unicode__(self):
    #     if self.leader:
    #         return u"s% (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
    #     else:
    #         return u"%s" % (self.title,)
