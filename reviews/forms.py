from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
