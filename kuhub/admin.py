from django.contrib import admin

from kuhub.models import Blog, BlogForum, Comment, BlogReport, CommentReport, Profile


admin.site.register(Blog)
admin.site.register(BlogForum)
admin.site.register(Comment)
admin.site.register(BlogReport)
admin.site.register(CommentReport)
admin.site.register(Profile)
