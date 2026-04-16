from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest
from .models import Post
from .check_post import is_bad_word

def home_view(request: HttpRequest):
    return redirect('main:posts_view')

def posts_view(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {"posts": posts})

def post_detail_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {"post": post})

def edit_post_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        if is_bad_word(title):
            return render(request, 'main/edit_post.html', {"post": post, "safe_title": False})
        if is_bad_word(content):
            return render(request, 'main/edit_post.html', {"post": post, "safe_content": False})

        image = request.FILES.get('image')
        post.title = title
        post.content = content
        if image:
            post.image = image
        post.save()
        return redirect('main:post_detail_view', post_id=post.id)

    return render(request, 'main/edit_post.html', {"post": post})

def delete_post_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('main:posts_view')
    return redirect('main:post_detail_view', post_id=post.id)

def create_post_view(request: HttpRequest):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if is_bad_word(title):
            return render(request, 'main/create_post.html', {"safe_title": False})
        if is_bad_word(content):
            return render(request, 'main/create_post.html', {"safe_content": False})
        image = request.FILES.get('image')
        new_post = Post(title=title, content=content)
        if image:
            new_post.image = image
        new_post.save()
        return redirect('main:posts_view')
    return render(request, 'main/create_post.html')

def mode_view(request: HttpRequest, mode: str):
    response = redirect(request.GET.get('next', '/'))

    if mode == 'light':
        response.set_cookie('mode', 'light')
    elif mode == 'dark':
        response.set_cookie('mode', 'dark')

    return response