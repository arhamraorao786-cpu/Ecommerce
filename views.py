from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
def Postblog(request):
    post=Blog.objects.get()
    return render(request,'blog/PostBlog.html',{'Post':post})