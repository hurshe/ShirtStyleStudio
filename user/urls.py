from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from views import Register, CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetCompleteView, profile, EditProfile
import views

urlpatterns = [
    path('', views.home, name='home'),
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
