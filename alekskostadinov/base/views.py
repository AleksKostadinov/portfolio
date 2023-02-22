from multiprocessing import context
from django.shortcuts import render

from base.models import Certificate, Work


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
    certificates = Certificate.objects.all()
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

def certificate(request, pk):
    certificate = Certificate.objects.get(id=pk)
    context = {
        'certificate': certificate,
    }
    return render(request, 'base/certificate.html', context)
