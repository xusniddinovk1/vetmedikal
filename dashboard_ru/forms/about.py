from django import forms

from medical_ru.models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service2
        fields = "__all__"


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature2
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact2
        fields = "__all__"


class InternetForm(forms.ModelForm):
    class Meta:
        model = Internet2
        fields = "__all__"


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission2
        fields = "__all__"


class MissionPointForm(forms.ModelForm):
    class Meta:
        model = MissionPoint2
        fields = "__all__"


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic2
        fields = "__all__"


class ValueForm(forms.ModelForm):
    class Meta:
        model = Value2
        fields = "__all__"


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement2
        fields = "__all__"


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member2
        fields = "__all__"


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History2
        fields = "__all__"
