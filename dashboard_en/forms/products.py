from django import forms
from medical_en.models import *


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory1
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product1
        fields = [
            "category",
            "title",
            "subtitle",
            "usage",
            "composition",
            "description",
            "image",
            "badge",
            "specs",
            "price",
            "country",
            "certificates",
        ]


class ProductFeatureForm(forms.ModelForm):
    class Meta:
        model = ProductFeature1
        fields = ["icon", "title", "description"]


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage1
        fields = ["product", "image"]
