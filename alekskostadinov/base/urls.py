from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('work/<slug:slug>/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('certificates/', views.certificates, name='certificates'),
    path('send_email/', views.send_email, name='send email'),
]
