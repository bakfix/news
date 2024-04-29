from django.contrib.auth import authenticate, login
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .models import News

class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class AllNewsListView(ListView):
    model = News
    template_name = 'all_news.html'
    context_object_name = 'all_news'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('all_news')  # Перенаправление на страницу всех новостей после успешного входа
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_news')  # Перенаправление на страницу с новостями после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        duration = request.POST.get('duration')
        # Обработка данных, например, сохранение в базу данных или выполнение других действий
        return render(request, ' registration.html')
    return render(request, 'subscription_form.html')

def all_news_view(request):
    all_news = News.objects.all()
    categories = News.objects.values_list('category', flat=True).distinct()  # Получаем список уникальных категорий
    return render(request, 'all_news.html', {'all_news': all_news, 'categories': categories})


def category_filter_view(request, category):
    print("Выбранная категория:", category)  # Добавим отладочное сообщение
    news_list = News.objects.filter(category=category)
    if not news_list:  # Если список новостей пуст
        print("Список новостей пуст!")
    return render(request, 'filtered_news.html', {'category': category, 'news_list': news_list})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(request):
    logout(request)
    return redirect('all_news')  # Замените 'index' на URL вашей главной страницы

def all_news(request):
    all_news = News.objects.all()
    user = request.user  # Получаем текущего пользователя

    return render(request, 'news_template.html', {'all_news': all_news, 'user': user})

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    # Здесь вы можете добавить код для получения дополнительной информации о пользователе
    return render(request, 'profile.html', {'user': user})
