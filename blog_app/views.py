from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import CreateView

from blog_app.forms import AddPostForm, AddPostFromBlogForm
from blog_app.models import Blog, Post

class IndexView(View):

    def get(self, request):
        return render(request, 'base.html', {'date':"DUPA"})


class IndexView2(View):

    def get(self, request):
        return render(request, 'cosnowego.html')


class AddBlog(View):

    def get(self, request):
        return render(request, 'manual_form.html')

    def post(self, request):
        name = request.POST['name']
        topic = request.POST['topic']
        Blog.objects.create(name=name, topic=topic)
        return redirect('add_blog')


class AddPostView(View):

    def get(self, request):
        form = AddPostForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            blog = form.cleaned_data['blog']
            Post.objects.create(text=text, blog=blog)
            return redirect('add_post')
        return render(request, 'form.html', {'form': form})


class ShowPost(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': Post.objects.all()})


class ShowBlog(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': Blog.objects.all()})


class ShowDetailBlog(View):

    def get(self, request, id):
        form = AddPostFromBlogForm()
        blog = Blog.objects.get(pk=id)
        return render(request, "blog_detail.html", {'blog': blog, 'form': form})

    def post(self, request, id):
        blog = Blog.objects.get(pk=id)
        form = AddPostFromBlogForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Post.objects.create(text=text, blog=blog)
            return redirect(f'/blog/{blog.id}/')
        return render(request, 'form.html', {'form': form})


class ShowDetailPost(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        return render(request, 'post_detail_view.html', {'post':post})
