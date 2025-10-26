from django import forms
from medical_ru.models import *


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory2
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product2
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
        model = ProductFeature2
        fields = ["icon", "title", "description"]


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage2
        fields = ["product", "image"]
