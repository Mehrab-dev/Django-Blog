from django import forms
from home.models import Newsletter

class NewsletterForm(forms.ModelForm) :
    class Meta :
        model = Newsletter
        fields = '__all__'