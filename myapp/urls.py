from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('index', views.index, name='home'),
    path('about', views.about, name='about'),
    path('maths', views.maths, name='maths'),
    path('class11', views.class11, name='class11'),
    path('class12', views.class12, name='class12'),
    path('class11-sets', views.class11sets, name='class11sets'),
    path('class11-physicalworld', views.class11physicalworld, name='class11physicalworld'),
    path('class12-relations', views.class12relations, name='class12-relations'),
    path('class12-ElectricChargesandField', views.class12electricchargesandfield, name='class12electricchargesandfield'),
    path('physics', views.physics, name='physics'),
    path('chemistry', views.chemistry, name='chemistry'),
    path('cs1', views.cs1, name='cs1'),
    path('cs2', views.cs2, name='cs2'),
    path('it', views.it, name='it'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handlelogin, name='handleloginin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('user', views.user, name='user'),
    path('contact', views.contact, name='contact'),
]