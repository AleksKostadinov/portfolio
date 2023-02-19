from django.shortcuts import render

def home(request):
    return render(request, 'base/index.html')

def works(request):
    return render(request, 'base/works.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def components(request):
    return render(request, 'base/components.html')

def work(request):
    return render(request, 'base/work.html')
