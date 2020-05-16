from .models import MainMenu ,Blog

def send_data(request):
    data ={
        'MenuData': MainMenu.objects.prefetch_related('blog_set').all(),
        'BlogData':Blog.objects.all(),
    }
    return data

