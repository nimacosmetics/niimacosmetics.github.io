from django.urls import path

from .import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('single/', views.single, name='single')
]