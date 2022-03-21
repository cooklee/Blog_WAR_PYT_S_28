from django import forms

from blog_app.models import Blog


class AddPostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    blog = forms.ModelChoiceField(queryset=Blog.objects.all())

class AddPostFromBlogForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())

