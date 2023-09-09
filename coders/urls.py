from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('test', views.test),
    path('result', views.result),
    path('aboutus', views.aboutus)

]