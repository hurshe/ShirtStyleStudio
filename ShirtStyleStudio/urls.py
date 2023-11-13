"""
URL configuration for ShirtStyleStudio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from user.views import Register, CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetCompleteView, profile, EditProfile, home
from shop.views import AllOffersReadView, OfferCreateView, OfferDeleteView, OfferUpdateView, ProductCreateView, AllProductReadView, ProductReadView, ProductUpdateView, ProductDeleteView, OfferDetailReadView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', Register.as_view(), name='registration'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', EditProfile.as_view(), name='edit_profile'),
    path('offer/<int:offer_id>/', OfferDetailReadView.as_view(), name='offer_details'),
    path('offers/', AllOffersReadView.as_view(), name='offers'),
    path('create_offer', OfferCreateView.as_view(), name='offer_create'),
    path('delete_offer/<int:pk>/', OfferDeleteView.as_view(), name='offer_delete'),
    path('update_offer/<int:offer_id>/', OfferUpdateView.as_view(), name='offer_update'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('products/', AllProductReadView.as_view(), name='products'),
    path('product/<int:product_id>/', ProductReadView.as_view(), name='product'),
    path('update_product/<int:product_id>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
