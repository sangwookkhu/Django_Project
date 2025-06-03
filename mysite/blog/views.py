# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 수정할 게시글 가져오기
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)  # 기존 객체와 함께 폼 생성
        if form.is_valid():
            form.save()  # 수정사항 저장
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  # GET 요청 시 기존 내용 채워진 폼 보여주기
    return render(request, 'blog/post_form.html', {'form': form})
