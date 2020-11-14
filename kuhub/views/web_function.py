from django.http import HttpResponseRedirect
from django.urls import reverse


def likes(request, pk, model):
    """Allowed user to like due to the conditions"""
    if model.dislikes.filter(id=request.user.id).exists():
        if not model.likes.filter(id=request.user.id).exists():
            model.dislikes.remove(request.user)
            model.likes.add(request.user)
            return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    elif model.likes.filter(id=request.user.id).exists():
        model.likes.remove(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    else:
        model.likes.add(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))


def dislikes(request, pk, model):
    """Allowed user to dislike due to the conditions"""
    if model.likes.filter(id=request.user.id).exists():
        if not model.dislikes.filter(id=request.user.id).exists():
            model.likes.remove(request.user)
            model.dislikes.add(request.user)
            return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    if model.dislikes.filter(id=request.user.id).exists():
        model.dislikes.remove(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
    else:
        model.dislikes.add(request.user)
        return HttpResponseRedirect(reverse('kuhub:blog-detail', args=[str(pk)]))
