from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('components/', views.components, name='components'),
    
    
]
