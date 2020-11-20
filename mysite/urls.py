"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from kuhub import views
from allauth.account import views as allauth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
      'accounts/password/change/',
      login_required(
          allauth_views.PasswordChangeView.as_view(
              success_url=reverse_lazy('kuhub:blog-home')
          )
      ),
      name='account_change_password'
    ),
    path(
      'accounts/password/set/',
      login_required(
          allauth_views.PasswordSetView.as_view(
              success_url=reverse_lazy('kuhub:blog-home')
          )
      ),
      name='account_change_password'
    ),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/<int:pk>/', views.ProfilePageView.as_view(), name='profile-page'),
    path('accounts/profile/edit', views.update_user, name='profile-edit'),
    path('', include('kuhub.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
