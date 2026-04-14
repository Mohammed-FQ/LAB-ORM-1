from django.shortcuts import render
from django.http import HttpRequest
from .models import Post

def home_view(request:HttpRequest):
    if request.method == "POST":
        new_post = Post(title = request.POST['title'], content = request.POST['content'])
        new_post.save()
    posts = Post.objects.all()
    return render(request, 'main/home.html',{"posts": posts})