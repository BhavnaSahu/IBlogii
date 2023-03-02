from django.shortcuts import render

# from Iblogiiee.blog.models import Post
from blog.models import Post,Category

# from Iblogiiee.blog.models import Category


def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    cats=Category.objects.all()
    data = {
        'posts': posts,
        'cats':cats,
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    return render(request, 'posts.html', {'post': post,'cats':cats})


def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})


