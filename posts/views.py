from .models import Post
from django.shortcuts import render, HttpResponse
import random


def home_page(request):
    return render(request, "base.html")

def first_view(request):
    random_figure = random.randint(1,100)
    response = f"america ya, {random_figure}"
    return HttpResponse(response)


def second_html_veiw(request):
    return render(request, "main.html")


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})
    
    
    
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", context={"post": post})