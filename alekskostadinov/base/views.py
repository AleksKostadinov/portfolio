from django.shortcuts import render
from base.forms import FormName
from base.models import Certificate, Work
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'base/index.html')


def works(request):
    works = Work.objects.order_by('id')
    context = {
        'works': works,
    }
    return render(request, 'base/works.html', context)


def about(request):
    return render(request, 'base/about.html')


def certificates(request):
    certificates = Certificate.objects.order_by('-date')
    context = {
        'certificates': certificates,
    }
    return render(request, 'base/certificates.html', context)


def work(request, slug):
    work = Work.objects.get(slug=slug)

    context = {
        'work': work,
    }
    return render(request, 'base/work.html', context)


def contact(request):
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success-url/')
    else:
        form = FormName()

    return render(request, 'base/contact.html', {'form': form})


def send_email(request):
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            template = render_to_string('base/email_template.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            })

            email = EmailMessage(
                form.cleaned_data['name'],
                template,
                settings.EMAIL_HOST_USER,
                ['kostadinov12@gmail.com']
            )
            email.fail_silently = False
            email.send()

            return render(request, 'base/email_sent.html')
    else:
        form = FormName()

    return render(request, 'base/contact.html', {'form': form})
