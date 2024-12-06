from django.shortcuts import render, get_object_or_404

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


@require_POST
def post_comment(request, post_id):
    pass
