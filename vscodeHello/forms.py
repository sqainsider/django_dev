from django import forms
from hello.models import LogMessage, Contact


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)  # NOTE: the trailing comma is required


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # NOTE: the trailing comma is required
        fields = ("lastName", "firstName")
