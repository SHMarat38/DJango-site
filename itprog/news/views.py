from django.shortcuts import render
from .models import News 
def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'main/news_home.html', {'news' :news})
