from django.views.generic import DetailView

from kuhub.forms import ExtendProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class ProfilePageView(DetailView):
    model = User
    template_name = 'kuhub/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data()
        locate = get_object_or_404(User, id=self.kwargs['pk'])

        context["locate"] = locate
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
