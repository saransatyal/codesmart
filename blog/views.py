from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Article , Author , Readarticle , Mythought ,Codeblog , Readcodeblog
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# hello world model
def base(request):
    return render(request,'base.html')
def archive(request):
    author_info = Author.objects.all()
    tips = Article.objects.all().order_by('-created_at')
    tutorials = Codeblog.objects.all().order_by('-created_at')
    return render(request,'archive.html',{'author_info':author_info, 'tips':tips,'tutorials':tutorials})

def codeblog(request):
    author_info = Author.objects.all()
    tutorials = Codeblog.objects.all().order_by('-created_at')
    return render(request,'codeblog.html',{'author_info':author_info, 'tutorials':tutorials})

def articles(request):
    author_info = Author.objects.all()
    tutorials = Article.objects.all().order_by('-created_at')
    return render(request,'articles.html',{'author_info':author_info, 'tutorials':tutorials})

def author_info(request):
    author_info = Author.objects.all()
    return render(request, 'author_info.html',{'author_info':author_info})

def readarticle(request, pk):
    author_info = Author.objects.all()
    tutorials = get_object_or_404(Article, pk=pk)
    tutorials.views += 1
    tutorials.save()
    return render(request, 'readarticle.html',{'tutorials':tutorials ,'author_info':author_info} )
def readcodeblog(request, pk):
    author_info = Author.objects.all()
    tutorials = get_object_or_404(Codeblog, pk=pk)
    tutorials.views += 1
    tutorials.save()
    return render(request, 'readcodeblog.html',{'tutorials':tutorials ,'author_info':author_info} )

def home(request):
    author_info = Author.objects.all()
    tips = Article.objects.all().order_by('created_at')
    tutorials = Codeblog.objects.all().order_by('created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(tutorials, 2)
    try:
        tutorials = paginator.page(page)
    except PageNotAnInteger:
        tutorials = paginator.page(1)
    except EmptyPage:
        tutorials = paginator.page(paginator.num_pages)
    read_article = Readarticle.objects.all().order_by('-updated_at')
    return render(request, 'home.html',{'author_info':author_info , 'tutorials':tutorials,'tips':tips, 'read_article':read_article})

def mythoughts(request):
    mythoughts = Mythought.objects.all()
    return render(request, 'mythoughts.html',{'mythoughts':mythoughts})
