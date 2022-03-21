from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from blog_app.models import Blog


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


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

class ShowBlog(View):

    def get(self, request):
        return render(request, 'blog_list.html', {'blogs':Blog.objects.all()})