
from django import forms

class StatusForm(forms.Form):
    text = forms.CharField(max_length = 300, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter status'}))


class CategoryForm(forms.Form):
    CHOICES = [('All', ''),
    ('Relatives', ''),
    ('Close Relatives', '')]

    trust_level = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
