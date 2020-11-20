from django.views.generic import DetailView

from kuhub.forms import ExtendProfileForm, UserProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.list import MultipleObjectMixin


class ProfilePageView(DetailView):
    model = User
    template_name = 'kuhub/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data()
        locate = get_object_or_404(User, id=self.kwargs['pk'])

        context["locate"] = locate
        return context


class UserBlogsListView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'kuhub/user_blogs.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        locate = get_object_or_404(User, id=self.kwargs['pk'])
        object_list = self.object.blogs.filter().order_by('-pub_date')

        context = super(UserBlogsListView, self).get_context_data(locate=locate, object_list=object_list, **kwargs)
        return context


@login_required
def update_user(request, **kwargs):
    profile_form = ExtendProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        profile_form = ExtendProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()

            return redirect('profile-page', pk=request.user.id)
    return render(request, 'kuhub/profile_edit.html', {'profile_form': profile_form})


@login_required
def create_profile(request, **kwargs):
    form = UserProfileForm()
    profile_form = ExtendProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ExtendProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('profile-page', pk=request.user.id)
    return render(request, 'kuhub/profile_create.html', {'form': form, 'profile_form': profile_form})
