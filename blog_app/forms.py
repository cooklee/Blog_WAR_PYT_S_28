from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Blog, Post, Comment


def check_length(value):
    if len(value) < 10:
        raise ValidationError("len < 10")


class AddPostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    blog = forms.ModelChoiceField(queryset=Blog.objects.all())


class AddPostFromBlogForm(forms.Form):
    number = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea(),validators=[check_length])

    def clean(self):
        data = super().clean()
        if 'text' not in data:
            return
        if len(data['text']) < data['number']:
            raise ValidationError("nie tędy droga kochany")
        return data

class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['blog', 'creation_date']


class AddCommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


