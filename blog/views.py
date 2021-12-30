from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import BlogPost
from .forms import BlogPostForm

def blog_posts(request):
    """ A view to return the main blog """
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)

def blog_detail(request, slug):
    """ A view that returns individual blog posts """
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'blog_post': blog_post,
    }
    return render(request, 'blog/blog_detail.html', context)

@login_required
def add_blog_post(request):
    """ A view to add blog posts to the blog """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Admin users have \
            access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            new_post.save()
            messages.success(request, 'Your blog post has been posted!')
            return redirect(reverse('blog_detail', args=[new_post.slug]))
        else:
            messages.error(request, 'Failed to post your blog post. Check that \
                the post is valid and try again.')
    else:
        form = BlogPostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_post.html', context)

@login_required
def edit_blog_post(request, slug):
    """ A view to edit existing blog posts in the blog """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Admin users have \
            access to this page!')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.author = request.user
            edit_post.slug = slugify(edit_post.title)
            form.save()
            messages.success(request, 'Your blog post has been updated!')
            return redirect(reverse('blog_detail', args=[edit_post.slug]))
        else:
            messages.error(request, 'Failed to update your blog post. Check that \
                the post is valid and try again.')
    else:
        form = BlogPostForm(instance=blog_post)
        messages.info(request, f'You are editing the blog post \
            "{blog_post.title}"')

    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, 'blog/edit_post.html', context)


@login_required
def delete_blog_post(request, slug):
    """ A view that deletes a chosen blog post from the blog """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Admin users have \
            access to this page!')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_post.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('blog'))