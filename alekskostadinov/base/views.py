from django.shortcuts import render

from base.models import Work


def home(request):
    return render(request, 'base/index.html')


def works(request):
    works = Work.objects.filter()[0:3]
    context = {
        'works': works,
    }
    return render(request, 'base/works.html', context)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def certificates(request):
    return render(request, 'base/certificates.html')


def work(request, pk):
    work = Work.objects.get(id=pk)
    context = {
        'work': work,
    }
    return render(request, 'base/work.html', context)
