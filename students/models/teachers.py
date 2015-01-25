# -*- coding: utf-8 -*-
from django.db import models

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
