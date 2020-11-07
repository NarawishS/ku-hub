from django.urls import path

from . import views

app_name = 'kuhub'
urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog-home'),
    path('blog/<int:pk>/', views.BlogView.as_view(), name='blog-detail'),
    path('create_blog', views.CreateBlogView.as_view(success_url="/"), name='create_blog'),
    path('like/<int:pk>', views.user_like, name='like_blog'),
    path('dislike/<int:pk>', views.user_dislike, name='dislike_blog'),
]
