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

    def get(self, request, *args, **kwargs):
        keyword = request.GET['keyword']
        blogs = self.model.objects.all()
        searched_blogs = []
        for blog in blogs:
            if keyword in blog.title or keyword in blog.text or keyword in str(blog.author):
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


class CreateBlogView(CreateView):
    model = Blog
    template_name = 'kuhub/create_blog.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
