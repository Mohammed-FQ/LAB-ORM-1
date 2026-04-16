from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post
from .check_post import is_bad_word

def home_view(request:HttpRequest):
    posts = Post.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if is_bad_word(title):
            print("not safe 1")
            return render(request, 'main/home.html',{"posts": posts, "safe_title": False})
        if is_bad_word(content):
            print("not safe 2")
            return render(request, 'main/home.html',{"posts": posts, "safe_content": False})
        image = request.FILES.get('image')
        new_post = Post(title=title, content=content)
        if image:
            new_post.image = image
        new_post.save()
        return render(request, 'main/home.html',{"posts": posts, "safe_title": True, "safe_content": True})
    return render(request, 'main/home.html',{"posts": posts})

def mode_view(request: HttpRequest, mode: str):
    response = redirect(request.GET.get('next', '/'))

    if mode == 'light':
        response.set_cookie('mode', 'light')
    elif mode == 'dark':
        response.set_cookie('mode', 'dark')

    return response