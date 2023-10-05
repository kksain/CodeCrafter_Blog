from django.shortcuts import render, HttpResponse
from blog.models import Post
# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    return render(request, 'blog/bloghome.html', {'allPosts' : allPosts})


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    context = {'post': post}
    
    return render(request, 'blog/blogpost.html' , context)
