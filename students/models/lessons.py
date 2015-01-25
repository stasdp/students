# -*- coding: utf-8 -*-
from django.db import models


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
