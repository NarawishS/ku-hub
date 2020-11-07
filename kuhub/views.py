from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from kuhub.models import Blog, Tag


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.request.GET['keyword']
        return context


class BlogView(DetailView):
    model = Blog
    template_name = 'kuhub/blog_detail.html'


class CreateBlogView(CreateView):
    model = Blog
    template_name = 'kuhub/create_blog.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
