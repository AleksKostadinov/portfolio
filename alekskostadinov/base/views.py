from django.shortcuts import render
from base.models import Certificate, Work
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    return render(request, 'base/index.html')


def works(request):
    works = Work.objects.all()
    context = {
        'works': works,
    }
    return render(request, 'base/works.html', context)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def certificates(request):
    certificates = Certificate.objects.order_by('-date')
    context = {
        'certificates': certificates,
    }
    return render(request, 'base/certificates.html', context)


def work(request, pk):
    work = Work.objects.get(id=pk)
    context = {
        'work': work,
    }
    return render(request, 'base/work.html', context)


def send_email(request):

    if request.method == 'POST':

        template = render_to_string('base/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['name'],
            template,
            settings.EMAIL_HOST_USER,
            ['kostadinov12@gmail.com']
        )
        email.fail_silently = False
        email.send()

    return render(request, 'base/email_sent.html')
