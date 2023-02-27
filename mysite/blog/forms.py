from django import forms
from .models import BlogModel

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        widget= forms.TextInput(attrs=
        {"placeholder": "Your title"}))
    content = forms.CharField(required=False,
    widget=forms.Textarea(
        attrs= {
            "placeholder": "Your description",
            "class" : "New-class-name two",
            "id" : "my-id",
            "rows" :12,
            "cols": 25,
        }
    ))
    image = forms.ImageField()
    class Meta:
        model= BlogModel
        fields = [
            'title', 'content','image',
        ]