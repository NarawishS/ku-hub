from django.urls import path

from . import views

app_name = 'kuhub'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.BlogHome.as_view(), name='blog-home')
]
