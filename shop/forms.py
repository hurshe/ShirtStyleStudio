from .models import Offer, Product
from django import forms


class OfferUpdateForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['product', 'price']


class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'size', 'qty', 'prod_img']


class ProductDeleteForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(ProductDeleteForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(user=user)

    rent = forms.ModelChoiceField(queryset=Product.objects.none())


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'size', 'qty', 'prod_img']
