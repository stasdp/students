# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u0430')),
                ('exam_group', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', blank=True, to='students.Group', null=True)),
            ],
            options={
                'verbose_name': '\u042d\u043a\u0437\u0430\u043c\u0435\u043d',
                'verbose_name_plural': '\u042d\u043a\u0437\u0430\u043c\u0435\u043d\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0434\u043c\u0435\u0442',
                'verbose_name_plural': '\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=256, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(verbose_name='\u042d\u043a\u0437\u0430\u043c\u0435\u043d\u0430\u0442\u043e\u0440', to='students.Teacher', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exam',
            name='title',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430', to='students.Lesson', max_length=256),
            preserve_default=True,
        ),
    ]
