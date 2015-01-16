from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from studentsdb.settings import ADMIN_EMAIL
    # TODO: Define form fields here
class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label = u"Ваш е-мейл адрес")

    subject = forms.CharField(
        label = u"Заголовок письма",
        max_length = 128)

    message = forms.CharField(
        label = u"Текст сообщения",
        max_length = 2560,
        widget = forms.TextArea)

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
                message = u'Сообщение успешно отослано!'
            #redirect to same contact page with success message
        return HttpResponseRedirect(
            u'%s? status_message=%s' % (reverse('contact_admin'), message))
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})
