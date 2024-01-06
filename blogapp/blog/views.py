from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog import models
from .models import Post

# Create your views here.
def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog.html', context)



def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/blog')
    
    return render(request, 'newpost.html')




def myPost(request):
    context = {
        'posts': Post.objects.filter(author= request.user)
    }
    return render(request, 'mypost.html', context)
