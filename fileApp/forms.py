from django import forms 

class EmailAttachementForm(forms.Form):
    mail_to = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))