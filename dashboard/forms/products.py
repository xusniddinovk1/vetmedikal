from django import forms
from medical.models import (
    ProductCategory,
    Product,
    ProductFeature,
    ProductImage,
)


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "title_uz",
            "title_ru",
            "title_en",
            "subtitle_uz",
            "subtitle_ru",
            "subtitle_en",
            "usage_uz",
            "usage_ru",
            "usage_en",
            "composition_uz",
            "composition_ru",
            "composition_en",
            "description_uz",
            "description_ru",
            "description_en",
            "image",
            "badge_uz",
            "badge_ru",
            "badge_en",
            "specs_uz",
            "specs_ru",
            "specs_en",
            "price",
            "country_uz",
            "country_ru",
            "country_en",
            "certificates_uz",
            "certificates_ru",
            "certificates_en",
        ]


class ProductFeatureForm(forms.ModelForm):
    class Meta:
        model = ProductFeature
        fields = "__all__"


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["product", "image"]
