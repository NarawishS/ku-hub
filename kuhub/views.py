from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from kuhub.models import Blog, Comment, BlogReport, CommentReport


def home(request):
    return render(request, "kuhub/home.html")


class BlogHome(ListView):
    model = Blog
    template_name = 'kuhub/index.html'
    context_object_name = "blog_entries"
    ordering = ['-pub_date']
    paginate_by = 3


class BlogSearch(ListView):
    model = Blog
    template_name = 'kuhub/search.html'
    context_object_name = "blog_entries"
    ordering = ['-pub_date']
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        keyword = request.GET['keyword']
        blogs = self.model.objects.all()
        searched_blogs = []
        for blog in blogs:
            if keyword in blog.title or keyword in blog.text or keyword in str(blog.author) \
                    or keyword in ' '.join([tag_name.name for tag_name in blog.tags.all()]):
                searched_blogs.append(blog)
        context = {
            self.context_object_name: searched_blogs,
            'keyword': keyword,
            'length': len(searched_blogs),
        }
        return render(request, self.template_name, context)


class BlogView(DetailView):
    model = Blog
    template_name = 'kuhub/blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        # look at the post and its id
        locate = get_object_or_404(Blog, id=self.kwargs['pk'])
        total_likes = locate.like_amount()
        total_dislikes = locate.dislike_amount()

        context = super(BlogView, self).get_context_data()

        check_liked = False

        if locate.likes.filter(id=self.kwargs['pk']):
            check_liked = True

        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        context['check_liked'] = check_liked
        return context


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'kuhub/create_blog.html'
    fields = ['title', 'text', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'kuhub/create_blog.html'
    fields = ['title', 'text', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


class CreateCommentView(CreateView):
    model = Comment
    template_name = 'kuhub/create_comment.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kuhub:blog-detail', kwargs={'pk': self.kwargs['pk']})


class BlogReportView(CreateView):
    model = BlogReport
    template_name = 'kuhub/blog_report.html'
    fields = ['topic', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kuhub:blog-detail', kwargs={'pk': self.kwargs['pk']})


class CommentReportView(CreateView):
    model = CommentReport
    template_name = 'kuhub/comment_report.html'
    fields = ['topic', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment_id = self.kwargs['ck']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kuhub:blog-detail', kwargs={'pk': self.kwargs['pk']})


class DeleteBlogView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


def user_like(request, pk):
    """Allowed user to like due to the conditions"""
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))

    if blog.dislikes.filter(id=request.user.id).exists():
        if not blog.likes.filter(id=request.user.id).exists():
            blog.dislikes.remove(request.user)
            blog.likes.add(request.user)
            return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    elif blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    else:
        blog.likes.add(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))


def user_dislike(request, pk):
    """Allowed user to dislike due to the conditions"""
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))

    if blog.likes.filter(id=request.user.id).exists():
        if not blog.dislikes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            blog.dislikes.add(request.user)
            return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    if blog.dislikes.filter(id=request.user.id).exists():
        blog.dislikes.remove(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    else:
        blog.dislikes.add(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
