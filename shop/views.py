from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Offer, Product
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from .forms import OfferUpdateForm, ProductUpdateForm, ProductDeleteForm, CreateProductForm, OfferForm
from django.db.models import Q


class OfferCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    fields = ['product', 'price']
    template_name = 'shop/offer_create.html'
    success_url = reverse_lazy('offer_create')

    def get_initial(self):
        initial = super().get_initial()
        initial['price'] = '00.00'
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OfferDetailReadView(View):
    template_name = 'shop/offer_detail.html'
    form_class = OfferForm

    def get(self, request, offer_id):
        offer = get_object_or_404(Offer, id=offer_id)
        form = self.form_class(instance=offer)
        return render(request, self.template_name, {'form': form, 'offer': offer})


class AllOffersReadView(View):

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Offer.objects.all()
        else:
            return Offer.objects.filter(user=self.request.user)
        
    def get(self, request):
        offers = self.get_queryset()
        return render(
            request, template_name='shop/all_offers.html',
            context={'offers': offers}
        )


class OfferUpdateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('offers')

    @staticmethod
    def get(request, offer_id):
        offer = get_object_or_404(Offer, pk=offer_id)
        form = OfferUpdateForm(instance=offer)
        return render(request, 'shop/offer_update.html', {'form': form, 'offer': offer})

    @staticmethod
    def post(self, request, offer_id):
        offer = get_object_or_404(Offer, pk=offer_id)
        form = OfferUpdateForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, 'shop/offer_update.html', {'form': form, 'offer': offer})


class OfferDeleteView(LoginRequiredMixin, DeleteView):
    model = Offer
    success_url = reverse_lazy('offers')
    template_name = 'shop/offer_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'product_create.html'
    success_url = '/products'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('products')

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductUpdateForm(instance=product)
        return render(request, 'shop/product_update.html', {'form': form, 'product': product})

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, 'shop/product_update.html', {'form': form, 'product': product})


class ProductDeleteView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        form = ProductDeleteForm(user=request.user)
        return render(request, 'product_delete.html', {'form': form})

    @staticmethod
    def post(request):
        form = ProductDeleteForm(request.user, request.POST)
        if form.is_valid():
            rent = form.cleaned_data['product']
            rent.delete()
            return redirect('products')
        return render(request, 'product_delete.html', {'form': form})


class AllProductReadView(LoginRequiredMixin, View):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.filter(user=self.request.user)

    def get(self, request):
        products = self.get_queryset()
        return render(
            request, template_name='shop/all_products.html',
            context={'products': products}
        )


class ProductReadView(LoginRequiredMixin, View):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.filter(user=self.request.user)

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(
            request, template_name='shop/product.html',
            context={'product': product}
        )


class Search(ListView):
    model = Offer
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Offer.objects.filter(
            Q(product__title__icontains=query) | Q(product__description__icontains=query)
        )
        return object_list

