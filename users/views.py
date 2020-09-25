from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration, UserUpdate, ProfileUpdate, AddPost, UpdatePost
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.core.paginator import Paginator


def signup(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'users/signup.html', {'form': form, 'title': 'signup'})


@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user.id).all().order_by('-date')
    paginator = Paginator(posts, 5)  # Show 5 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        user_update = UserUpdate(request.POST, instance=request.user)
        profile_update = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        post_add = AddPost(request.POST, request.FILES)

        if user_update.is_valid() and profile_update.is_valid():
            user_update.save()
            profile_update.save()
            messages.success(request, f'Your account have been updated!')

        if post_add.is_valid():
            post_add.Author = request.user
            post_add.save()
            messages.success(request, f'Post added successfully!')
        return redirect('profile')
    else:
        user_update = UserUpdate(instance=request.user)
        profile_update = ProfileUpdate(instance=request.user.profile)
        post_add = AddPost()

    context = {
        'posts': page_obj,
        'user_update_form': user_update,
        'profile_update_form': profile_update,
        'title': 'profile',
        'post_add': post_add
    }
    return render(request, 'users/profile.html', context)


@login_required
def deletepost(request, id):
    Post.objects.get(id=id).delete()
    return redirect('profile')


@login_required
def Updatepost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        update_post = UpdatePost(request.POST, request.FILES, instance=post)
        if update_post.is_valid():
            update_post.save()
            messages.success(request, f'Post updated successfully!')
        return redirect('profile')
    else:
        update_post = UpdatePost(instance=post)

    context = {
        'update_post': update_post,
        'title': 'edit'
    }
    return render(request, 'users/edit.html', context)
