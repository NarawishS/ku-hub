from django.urls import path

from . import views

app_name = 'kuhub'
urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog-home'),
    path('blog/<int:pk>/', views.BlogView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/create_comment', views.CreateCommentView.as_view(), name='create_comment'),
    path('create_blog', views.CreateBlogView.as_view(success_url="/"), name='create_blog'),
]
