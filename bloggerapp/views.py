from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import BlogPost, UserProfile
from .forms import BlogPostForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from .models import Post, User
from django.http import JsonResponse
from .forms import UserProfileForm
from django.contrib.auth.models import User




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def post_list(request):
    posts = BlogPost.objects.order_by('?')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def edit_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('view_profile')
    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'bloggerapp/edit_profile.html', {'profile_form': profile_form})


@login_required
def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    user_posts = BlogPost.objects.filter(author=user)

    return render(request, 'bloggerapp/view_profile.html', {'user': user, 'user_profile': user_profile, 'user_posts': user_posts})


@login_required
def delete_post(request, pk):
    # Retrieve the post object from the database using the primary key (pk)
    post = get_object_or_404(BlogPost, pk=pk)

    # Check if the user is authenticated and the author of the post
    if request.user.is_authenticated and request.user == post.author:
        if request.method == 'POST':
            # If the request method is POST, it means the user has confirmed the deletion.
            # Delete the post and redirect to the post list page or another appropriate page.
            post.delete()
            return redirect('post_list')
        else:
            # If the request method is GET, render the confirmation template.
            return render(request, 'delete_post.html', {'post': post})
    else:
        # If the user is not authenticated or not the author of the post, redirect to a permission denied page or login page.
        return redirect('post_list')  # Replace 'permission_denied' with the appropriate URL or view name.
    

def logout_user(request):
    logout(request)
    return redirect('login')