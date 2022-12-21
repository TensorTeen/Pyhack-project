
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('test',views.test, name='test'),
    path('train',views.train, name='train'),

]