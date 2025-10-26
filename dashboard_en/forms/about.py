from django import forms
from medical_en.models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service1
        fields = "__all__"


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature1
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact1
        fields = "__all__"


class InternetForm(forms.ModelForm):
    class Meta:
        model = Internet1
        fields = "__all__"


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission1
        fields = "__all__"


class MissionPointForm(forms.ModelForm):
    class Meta:
        model = MissionPoint1
        fields = "__all__"


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic1
        fields = "__all__"


class ValueForm(forms.ModelForm):
    class Meta:
        model = Value1
        fields = "__all__"


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement1
        fields = "__all__"


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member1
        fields = "__all__"


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History1
        fields = "__all__"
