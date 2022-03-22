from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Blog

def check_length(value):
    if len(value) < 50:
        raise ValidationError("NIe bede obsługiwał tak krótkich postów")


class AddPostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    blog = forms.ModelChoiceField(queryset=Blog.objects.all())

class AddPostFromBlogForm(forms.Form):
    number = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea(), validators=[check_length])

