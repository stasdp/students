# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from contact_form.forms import ContactForm
from django.views.generic.edit import FormView
# from contact_form.views import ContactFormView 

# class ContactView(FormView):
#     template_name = 'contact_admin/form.html'
#     form_class = ContactForm
#     success_url = '/contact-admin/'

#     def form_valid(self, form):
#         #This method is called for valid data
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']
#         from_email = form.cleaned_data['from_email']

#         send_mail(subject, message, from_email, ['staspanuta@gmail.com'])

#         return super(ContactView, self).form_valid(form)

    # TODO: Define form fields here

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        #call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)
        #this helper object allows use to customize form
        self.helper = FormHelper()
        #from tag attr
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')
        #twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        #form buttons
        self.helper.add_input(Submit('send_button', u'Отправить'))

    from_email = forms.EmailField(
        label = u"Ваш е-мейл адрес")

    subject = forms.CharField(
        label = u"Заголовок письма",
        max_length = 128)

    message = forms.CharField(
        label = u"Текст сообщения",
        max_length = 2560,
        widget = forms.Textarea)

def contact_admin(request):
    #check  if form was posted
    if request.method == 'POST':
        #create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        #check whether user data is valid
        if form.is_valid():
            #send mail
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])

            except Exception:
                message = u'Во время отправки письма случилась непредсказуемая ошибка.Попробуйте воспользоваться позже.'

            else:
                message = u'Сообщение успешно отправлено!'
            #redirect to same contact page with success message
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('contact_admin'), message))

    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})

# class ContactForm(forms.contact_form):
#     def __init__(self, *args, **kwargs):
#         #call original initializator
#         super(ContactForm, self).__init__(*args, **kwargs)
#         #this helper object allows use to customize form
#         self.helper = FormHelper()
#         #from tag attr
#         self.helper.form_class = 'form-horizontal'
#         self.helper.form_method = 'post'
#         self.helper.form_action = reverse('contact_admin')
#         #twitter bootstrap styles
#         self.helper.help_text_inline = True
#         self.helper.html5_required = True
#         self.helper.label_class = 'col-sm-2 control-label'
#         self.helper.field_class = 'col-sm-10'
#         #form buttons
#         self.helper.add_input(Submit('send_button', u'Отправить'))

#     from_email = forms.EmailField(
#         label = u"Ваш е-мейл адрес")

#     subject = forms.CharField(
#         label = u"Заголовок письма",
#         max_length = 128)

#     message = forms.CharField(
#         label = u"Текст сообщения",
#         max_length = 2560,
#         widget = forms.Textarea)
