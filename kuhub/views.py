from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from kuhub.models import Blog
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from kuhub.models import Blog, Comment


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


class CreateBlogView(CreateView):
    model = Blog
    template_name = 'kuhub/create_blog.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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



