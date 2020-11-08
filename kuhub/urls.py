from django.urls import path

from . import views

app_name = 'kuhub'
urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog-home'),
    path('blog/<int:pk>/', views.BlogView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/create_comment', views.CreateCommentView.as_view(), name='create_comment'),
    path('blog/<int:pk>/blog_report', views.BlogReportView.as_view(), name='blog_report'),
    path('blog/<int:pk>/comment/<int:ck>/comment_report', views.CommentReportView.as_view(), name='comment_report'),
    path('blog/<int:pk>/delete', views.DeleteBlogView.as_view(), name='blog-delete'),
    path('blog/<int:pk>/update', views.UpdateBlogView.as_view(), name='blog-update'),
    path('create_blog', views.CreateBlogView.as_view(success_url="/"), name='create_blog'),
    path('search', views.BlogSearch.as_view(), name='blog-search'),
    path('like/<int:pk>', views.user_like, name='like_blog'),
    path('dislike/<int:pk>', views.user_dislike, name='dislike_blog'),
]
