from django.shortcuts import render, HttpResponse
import random


def first_view(request):
    random_figure = random.randint(1,100)
    response = f"america ya, {random_figure}"
    return HttpResponse(response)

def html_view(request):
    return render(request, "base.html")


def second_html_veiw(request):
    return render(request, "main.html")