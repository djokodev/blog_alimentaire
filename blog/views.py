from django.shortcuts import render
from django.http import HttpResponse
from . models import Article

def home(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "index.html", context=context)