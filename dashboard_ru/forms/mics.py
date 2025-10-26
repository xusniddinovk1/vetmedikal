from django.contrib.auth import get_user_model
from django import forms
from medical_ru.models import *

User = get_user_model()


class ProfileForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'bio', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter bio'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ManufacturingOverviewForm2(forms.ModelForm):
    class Meta:
        model = ManufacturingOverview2
        fields = "__all__"


class ManufacturingStatForm(forms.ModelForm):
    class Meta:
        model = ManufacturingStat2
        fields = "__all__"


class ProductionLineForm(forms.ModelForm):
    class Meta:
        model = ProductionLine2
        fields = "__all__"


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner2
        fields = "__all__"


class PartnershipBenefitForm(forms.ModelForm):
    class Meta:
        model = PartnershipBenefit2
        fields = "__all__"


class GalleryCategoryForm(forms.ModelForm):
    class Meta:
        model = GalleryCategory2
        fields = "__all__"


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery2
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category2
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News2
        fields = "__all__"
