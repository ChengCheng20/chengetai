from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='service'),
    path('contact.html', views.contact, name='contact'),
]