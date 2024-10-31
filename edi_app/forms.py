# edi_app/forms.py
from django import forms
from edi_app.models import EDIMessage

class EDIMessagesForm(forms.ModelForm):
    class Meta:
        model = EDIMessage
        fields = ['sender', 'receiver', 'document_type', 'document_data']
