from django.urls import path

from . import views

app_name = 'kuhub'
urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog-home'),
    path('blog/<int:pk>/', views.BlogView.as_view(), name='blog-detail'),
    path('forum', views.BlogForumIndexView.as_view(), name='blog-forum-index'),
    path('forum/<int:pk>/delete', views.delete_blog_forum, name='blog-forum-delete'),
    path('forum/<int:pk>/', views.BlogForumView.as_view(), name='blog-forum'),
    path('blog/<int:pk>/create_comment', views.CreateCommentView.as_view(), name='create_comment'),
    path('blog/<int:pk>/blog_report', views.BlogReportView.as_view(), name='blog_report'),
    path('blog/<int:pk>/comment/<int:ck>/comment_report', views.CommentReportView.as_view(), name='comment_report'),
    path('comment/<int:pk>/delete', views.DeleteCommentView.as_view(), name='comment-delete'),
    path('blog/<int:pk>/delete', views.DeleteBlogView.as_view(), name='blog-delete'),
    path('blog/<int:pk>/update', views.UpdateBlogView.as_view(), name='blog-update'),
    path('create_blog', views.CreateBlogView.as_view(success_url="/"), name='create_blog'),
    path('search', views.BlogSearch.as_view(), name='blog-search'),
    path('like/<int:pk>', views.user_like, name='like_blog'),
    path('dislike/<int:pk>', views.user_dislike, name='dislike_blog'),
    path('blog/<int:pk>/like_comment', views.comment_like, name='like_comment'),
    path('blog/<int:pk>/dislike_comment', views.comment_dislike, name='dislike_comment'),
    path('tags/', views.BlogTagsIndex.as_view(), name='tag_list'),
    path('tags/list', views.BlogTagsSearch.as_view(), name='tag_blog'),
]
