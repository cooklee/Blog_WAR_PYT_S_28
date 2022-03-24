from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from blog_app.forms import AddPostForm, AddPostFromBlogForm, AddPostModelForm, AddCommentModelForm
from blog_app.models import Blog, Post

class IndexView(View):

    def get(self, request):
        return render(request, 'base.html', {'date':"DUPA"})


class IndexView2(View):

    def get(self, request):
        return render(request, 'cosnowego.html')


class AddBlog(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'manual_form.html')

    def post(self, request):
        name = request.POST['name']
        topic = request.POST['topic']
        Blog.objects.create(name=name, topic=topic, author=request.user)
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
        form = AddPostModelForm()
        blog = Blog.objects.get(pk=id)
        return render(request, "blog_detail.html", {'blog': blog, 'form': form})

    def post(self, request, id):
        blog = Blog.objects.get(pk=id)
        form = AddPostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
            return redirect(f'/blog/{blog.id}/')
        return render(request, 'form.html', {'form': form})


class ShowDetailPost(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        return render(request, 'post_detail_view.html', {'post':post})

class UpdatePostView(View):

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        form = AddPostModelForm(instance=post)
        return render(request, 'form.html', {'form':form})

    def post(self, request, id):
        post = Post.objects.get(pk=id)
        form = AddPostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse("update_post"), args=[id])
        return render(request, 'form.html', {'form': form})

class DeletePostView(View):

    def get(self, request, id):
        # post = Post.objects.get(pk=id)
        return render(request, 'form.html', {})

    def post(self, request, id):
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect('show_post')


class AddCommentView(View):

    def get(self, request):
        form = AddCommentModelForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = AddCommentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})