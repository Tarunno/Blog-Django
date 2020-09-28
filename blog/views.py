from django.shortcuts import render, redirect
from .models import Post, Category, Comment, Trending
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import AddComment
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    posts = Post.objects.all().order_by('-date')
    categories = Category.objects.all()
    paginator = Paginator(posts, 4)  # Show 4 posts per page.

    trendings = Trending.objects.filter(trending=True).all()[0:3]

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'categories': categories,
        'trendings': trendings
    }
    return render(request, 'blog/home.html', context)


def about(request):
    users = User.objects.all()
    context = {
        'users': users,
        'title': 'about'
    }
    return render(request, 'blog/about.html', context)


def single(request, id):
    posts = Post.objects.get(id=id)
    comments = posts.comments.all().order_by('-date')

    category = posts.category
    relateds = Post.objects.filter(category=category).all().order_by('-date')[:3]

    if request.method == 'POST':
        comment_frm = AddComment(request.POST)
        if comment_frm.is_valid():
            comment_frm.save()
            messages.success(request, f'Comment added successfully!')
            return redirect('single', id=id)
        else:
            messages.error(request, f'commenting error occurs!')
    else:
        comment_frm = AddComment()

    context = {
        'posts': posts,
        'comment_frm': comment_frm,
        'comments': comments,
        'relateds': relateds,
        'title': 'post'
    }
    return render(request, 'blog/single.html', context)


def Categoryhome(request, id):
    posts = Post.objects.filter(category_id=id).all().order_by('-date')
    categories = Category.objects.all()
    paginator = Paginator(posts, 3)  # Show 3 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'categories': categories
    }
    return render(request, 'blog/category-home.html', context)


def delete_comment(request, id, del_id):
    posts = Post
    posts = posts.objects.get(id=id)
    comments =  Comment
    comment = comments.objects.get(id=del_id)
    if request.method == 'GET':
        comment.delete()
        return redirect('single', id=id)
    return render(request, 'blog/single.html')


def like(request, id, user):
    posts = Post
    posts = posts.objects.get(id=id)
    if request.method == 'GET':
        posts.likes.add(user)
    likes = posts.likes.count()
    print(likes)
    return JsonResponse({'like': 'false', 'likes': likes}, safe=False)


def unlike(request, id, user):
    posts = Post
    posts = posts.objects.get(id=id)
    if request.method == 'GET':
        posts.likes.remove(user)
    likes = posts.likes.count()
    print(likes)
    return JsonResponse({'like': 'true', 'likes': likes}, safe=False)
