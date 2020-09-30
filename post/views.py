from django.shortcuts import render, redirect
from .models import Post
from account.models import User 
from django.http import HttpResponse

# Create your views here.

def post(request):
    post_instance = Post.objects.all()
    return render(request, 'post/post.html', {"posts": post_instance})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        username = request.session['user']
        user = User.objects.filter(username=username)
        post = Post.objects.create(title=title, body=body)
        post.author_id.set(user)
        post.save()
        return redirect('post')
    return render(request, 'post/create.html')

def getbyid(request, id):
    post = Post.objects.filter(id=id)
    if post.exists():
        return render(request, 'post/detail.html', {"post": post})
    else:
        return redirect('post')

def update(request):
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        body = request.POST['body']
        session_user = request.session['user']

        user = User.objects.get(username=session_user)
        post = Post.objects.get(id=id)
        
        user_list = []
        for author_id in post.author_id.all():
            user_list.append(author_id)

        user_list.append(user)
        post.author_id.set(user_list)
        return redirect('post')
    return redirect('post')

def delete(request, id):
    post = Post.objects.get(id=id).delete()
    print(post)
    return redirect('post')