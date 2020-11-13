from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from kuhub.models import Comment, CommentReport
from kuhub.views.web_function import likes, dislikes


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'kuhub/create_comment.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kuhub:blog-detail', kwargs={'pk': self.kwargs['pk']})


class CommentReportView(LoginRequiredMixin, CreateView):
    model = CommentReport
    template_name = 'kuhub/comment_report.html'
    fields = ['topic', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment_id = self.kwargs['ck']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kuhub:blog-detail', kwargs={'pk': self.kwargs['pk']})


class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


@login_required(redirect_field_name='blog-detail')
def comment_like(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    return likes(request, pk, comment)


@login_required(redirect_field_name='blog-detail')
def comment_dislike(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    return dislikes(request, pk, comment)
