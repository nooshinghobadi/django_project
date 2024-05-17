from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
    posts=Post.published.all()
    return render(request,
                  'firstblog/post/list.html',
                  {'posts':posts})
def post_detail(request, id):
    #try:
        #post=Post.published.get(id=id)
    #except Post.DoesNotExist:
        #raise Http404("No post found.")
    post=get_object_or_404(Post,
                           id=id,
                           status=Post.Status.published)
    
    return render(request,
                  'firstblog/post/detail.html',
                  {'post':post})

