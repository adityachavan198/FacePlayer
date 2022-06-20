from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('photodetect', views.photodetect, name='photodetect'),
    path("signupform", views.signupform, name="signupform"),
    path("signupsubmit", views.signupsubmit, name="signupsubmit"),
    path("loginform", views.loginform, name="loginform"),
    path("loginsubmit", views.loginsubmit, name="loginsubmit"),
 
]
