from django.shortcuts import render, redirect,reverse
from .models import MainMenu, Blog, Like
from django.core.paginator import Paginator
from .forms import CreateBlog
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    contact_list = Blog.objects.all()
    paginator = Paginator(contact_list, 3)
    page = request.GET.get('page')
    menuData = paginator.get_page(page)
    query = request.GET.get('q')

    if query:
        menuData =Blog.objects.filter(       #Search ko lagi
            Q(title__icontains=query) |
            Q(author__username=query) |
            Q(description__icontains=query)
        )
    data = {
        'allData': menuData,
    }

    return render(request, 'pages/index.html', data)


def category(request, category):
    contact_list = Blog.objects.filter(main_menu__name=category)
    paginator = Paginator(contact_list, 10)
    page = request.GET.get('page')
    category_data = paginator.get_page(page)
    query = request.GET.get('q')
    if query:
        category_data = Blog.objects.filter(   #search ko lagi
            Q(title__icontains=query) |
            Q(author__username=query) |
            Q(description__icontains=query)
        )
    data = {
        # 'menuDetails': MainMenu.objects.get(slug=slug),
        'title': MainMenu.objects.get(name=category),
        'total_posts_by_category': category_data,
    }
    return render(request, 'pages/quotes/blog.html', data)

def single(request, slug):
    data = {
        'postDetails': Blog.objects.get(slug=slug),
        'title': Blog.objects.get(slug=slug)
    }
    return render(request, 'pages/quotes/post.html', data)


def about(request):
    data = {
        'title': 'About'
    }
    return render(request, 'pages/about.html', data)


def contact(request):
    data = {
        'title': 'Contact'
    }
    return render(request, 'pages/contact.html', data)


def create_blog(request):
    form = CreateBlog()
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.info(request, "Quotes has been successfully send to Admin, Send Another ")
            return redirect('createblog')
        else:
            messages.info(request, " Title Should be in English ")

    return render(request, 'pages/quotes/createblog.html', {'form': form})


def profile(request,username):
    data = {
        'profiledata' : Blog.objects.filter(author__username = username)
    }
    return render(request,'pages/quotes/profile.html',data)

def liked_post(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            blog_id = request.POST.get('blog_id')
            quotes = Blog.objects.get(id= blog_id)

            if user in quotes.thumbup.all():
                quotes.thumbup.remove(user)
            else:
                quotes.thumbup.add(user)

            like, created =  Like.objects.get_or_create(user=user, post_id =blog_id)

            if not created:
                if like.value =='like':
                    like.value == "Unlike"
                else:
                    like.value =='like'
            like.save()
    return redirect(reverse('category', kwargs={
        'category':quotes.main_menu.name }))

