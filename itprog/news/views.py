from django.shortcuts import render

def news_home(request):
    return render(request, 'main/news_home.html')
