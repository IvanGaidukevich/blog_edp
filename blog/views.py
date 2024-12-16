from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def get_post(request, year, month, day, slug):
    post = get_object_or_404(Post, published__year=year, published__month=month, published__day=day, slug=slug)
    comments = post.comments.all()
    form = CommentForm()
    return render(request, 'blog/post/post.html', {'post': post, 'comments': comments, 'form': form})


@login_required
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = None
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return redirect('accounts:login')
    if request.method == 'POST':
        comment.delete()
        return redirect(comment.post.get_absolute_url())
    return render(request, 'blog/post/delete_comment_confirm.html', {'comment': comment})

