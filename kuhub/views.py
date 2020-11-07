from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from kuhub.models import Blog


def home(request):
    return render(request, "kuhub/home.html")


class BlogHome(ListView):
    model = Blog
    template_name = 'kuhub/index.html'
    context_object_name = "blog_entries"
    ordering = ['-pub_date']
    paginate_by = 3


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
