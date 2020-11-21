from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from taggit.models import Tag

from kuhub.forms import BlogForm
from kuhub.models import Blog, BlogReport, BlogForum
from kuhub.views.web_function import likes, dislikes


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
            if keyword.lower() in blog.title.lower() \
                    or keyword.lower() in blog.short_description.lower() \
                    or keyword.lower() in blog.body.lower() \
                    or keyword.lower() in str(blog.author).lower() \
                    or keyword.lower() in ' '.join([tag_name.name for tag_name in blog.tags.all()]).lower():
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

        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        return context


class BlogForumIndexView(ListView):
    model = BlogForum
    template_name = 'kuhub/forum_index.html'
    context_object_name = "blog_forums"


class BlogTagsIndex(ListView):
    model = Tag
    template_name = 'kuhub/tags_index.html'
    ordering = ['name']
    context_object_name = "tag_list"
    paginate_by = 10


class BlogTagsSearch(ListView):
    model = Blog
    template_name = 'kuhub/tags_list.html'
    context_object_name = "blog_entries"
    ordering = ['-pub_date']
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        keyword = request.GET['keyword']
        blogs = self.model.objects.all()
        searched_blogs = []
        for blog in blogs:
            if keyword.lower() in ' '.join([tag_name.name for tag_name in blog.tags.all()]).lower():
                searched_blogs.append(blog)
        context = {
            self.context_object_name: searched_blogs,
            'keyword': keyword,
            'length': len(searched_blogs),
        }
        return render(request, self.template_name, context)


class BlogForumView(ListView):
    model = Blog
    template_name = 'kuhub/forum_detail.html'
    context_object_name = "blog_entries"
    ordering = ['-pub_date']
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        forum = BlogForum.objects.get(id=self.kwargs.get('pk'))
        blogs = Blog.objects.filter(forum_id=self.kwargs.get('pk'))
        return {'forum': forum, self.context_object_name: blogs}


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'kuhub/create_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteBlogView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'kuhub/create_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


class BlogReportView(LoginRequiredMixin, CreateView):
    model = BlogReport
    template_name = 'kuhub/blog_report.html'
    fields = ['topic', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kuhub:blog-detail', kwargs={'pk': self.kwargs['pk']})


@login_required(redirect_field_name='blog-detail')
def user_like(request, pk):
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))
    return likes(request, pk, blog)


@login_required(redirect_field_name='blog-detail')
def user_dislike(request, pk):
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))
    return dislikes(request, pk, blog)
