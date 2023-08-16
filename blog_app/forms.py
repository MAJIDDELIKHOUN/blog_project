from django import forms
from .models import Contact_Us
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=70)
    subject = forms.CharField(max_length=70)
    email = forms.EmailField()
    body = forms.CharField()

    def clean(self):
        name = self.cleaned_data.get('name')
        subject = self.cleaned_data.get('subject')
        if name == subject:
            raise ValidationError('same name subject', code=256)
        # if 'f' in name:
        #     self.add_error('name','f not e')

    # def clean_subject(self):
    #  subject = self.cleaned_data.get('subject')
    #  if 'f' in subject:
    #     raise ValidationError('f not be here', code='heyyy')
    #  return subject
