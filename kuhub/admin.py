from django.contrib import admin

from kuhub.models import Blog, Tag, Comment, BlogReport, CommentReport

admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogReport)
admin.site.register(CommentReport)
