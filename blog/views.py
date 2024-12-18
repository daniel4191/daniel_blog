from PIL.ImageFilter import DETAIL
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post, Category, Tag


# Create your views here.

# CBV 스타일
# Listview를 받아 사용하는 CBV 스타일은 모델명 뒤에 _list가 붙은 html 파일이여야 리드가 된다.
# 혹은 views에서 template_name을 지정해서 변경해주는 방식이 사용 가능하다.
class PostList(ListView):
    model = Post
    ordering = "-pk"
    # Listview 사용방법으로써, 기존에 사용하던 파일명 변경하기 싫을 때, 지정해준다.
    # app이름/모델명_list.html 구조여야한다.
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DeleteView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    template_name = "blog/post_detail.html"


# FBV 스타일
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        "blog/post_list.html",
        {
            "post_list": post_list,
            "tag":tag,
            "categories" : Category.objects.all(),
            "no_category_post_count" : Post.objects.filter(category=None).count()
        }
    )

def category_page(request, slug):

    if slug == "no_category":
        category = "미분류"
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request, "blog/post_list.html",
        {
            "post_list": post_list,
            "categories": Category.objects.all(),
            "no_category_post_count": Post.objects.filter(category=None).count(),
            "category": category
        }
    )

"""
def index(request):
    posts = Post.objects.all().order_by("-pk")

    return render(
        request, 'blog/post_list.html',
        {
            'posts':posts
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request, "blog/post_detail.html",
        {
            'post':post
        }
    )
"""
