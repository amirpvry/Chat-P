from django import forms
from APPSAMPLE.models import contact
from captcha.fields import CaptchaField


class NameForm(forms.Form):
    name = forms.CharField(label="name", max_length=255)
    email = forms.EmailField(label="email", max_length=255)
    subject = forms.CharField(label="subject", max_length=255)
    message = forms.CharField(label="message", widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'message']