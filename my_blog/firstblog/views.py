from django.shortcuts import render, get_object_or_404
from .models import Post , Comment
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm , CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count


def post_list(request, tag_slug=None):
    post_list=Post.published.all()
    tag =None
    if tag_slug:
        tag=get_object_or_404(Tag, slug=tag_slug)
        post_list= post_list.filter(tags__in=[tag])
    ##paigination with 3 posts per page
    paginator=Paginator(post_list, 3)
    page_number=request.GET.get('page', 1)
    try:
        posts=paginator.page(page_number)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        ##if page_number isnt exist deliver last page
        posts=paginator.page(paginator.num_pages)

    return render(request,
                  'firstblog/post/list.html',
                  {'posts':posts,
                   'tag':tag})

#class PostListView(ListView):
    #queryset=Post.published.all()
    #context_object_name='posts'
    #paginate_by=3
    #template_name='firstblog/post/list.html'

def post_detail(request, year, month, day, post):
    #try:
        #post=Post.published.get(id=id)
    #except Post.DoesNotExist:
        #raise Http404("No post found.")
    post=get_object_or_404(Post,
                           status=Post.Status.published,
                           slug=post,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    
    comments=post.comments.filter(active=True)
    form=CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in = post_tags_ids)\
                                          .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags','-publish')[:4]

    return render(request,
                  'firstblog/post/detail.html',
                  {'post':post,
                   'comments':comments,
                   'form':form,
                   'similar_posts':similar_posts})

def post_share(request, post_id):
    post=get_object_or_404(Post, id=post_id, status=Post.Status.published)
    sent = False

    if request.method == 'POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url = request.build_absolute_uri(
                       post.get_absolute_url())
            subject = f"{cd['name']} recommends you read "\
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'nooshinghobadi0@gmail.com',
                      [cd['to']])
            sent = True
    else:
        form=EmailPostForm()
    return render(request, 'firstblog/post/share.html',
                            {'post':post,'form':form,'sent': sent})

@require_POST
def post_comment(request, post_id):
    post=get_object_or_404(Post, id=post_id, status=Post.Status.published)
    comment=None
    form=CommentForm(data=request.POST)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post=post
        comment.save()
    return render(request, 'firstblog/post/comment.html',
                  {'post':post,
                  'form':form,
                  'comment':comment})
