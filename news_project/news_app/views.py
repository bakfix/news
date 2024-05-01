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
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import CommentForm
from django.shortcuts import render
from .models import News

from urllib.parse import unquote

def news_by_city(request):
    global city
    city_encoded = request.GET.get('city', '')  # Получаем закодированное значение города
    if city_encoded is not None:
        city = unquote(city_encoded)  # Декодируем его
        print("Выбранный город:", city)  # Отладочный вывод для города
        if city:  # Если город выбран
            # Получаем новости для этого города и сортируем их по убыванию просмотров
            news = News.objects.filter(city=city).order_by('-views')
            print("Новости для выбранного города:", news)  # Отладочный вывод для новостей
        else:  # Если город не выбран, показываем все новости
            news = News.objects.all().order_by('-views')

    else:
        news = News.objects.all()
    return render(request, 'all_news.html', {'news': news, 'city': city})


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
    selected_city = request.GET.get('city')  # Получаем выбранный город из запроса
    if selected_city:  # Если город выбран
        news_list = News.objects.filter(category=category, city=selected_city)
    else:  # Если город не выбран, фильтруем только по категории
        news_list = News.objects.filter(category=category)

    # Передача выбранного города в контекст шаблона
    return render(request, 'filtered_news.html', {'category': category, 'news_list': news_list, 'selected_city': selected_city})

# def category_filter_view(request, category):
#     cityy = request.GET.get('city')  # Получаем значение города из запроса
#     print("Selected city:", cityy)  # Отладочный вывод для города
#     print("Выбранная категория:", category)  # Добавим отладочное сообщение
#     news_list = News.objects.filter(category=category, city=cityy)  # Фильтруем новости по категории и городу
#     if not news_list:  # Если список новостей пуст
#         print("Список новостей пуст!")
#     return render(request, 'filtered_news.html', {'category': category, 'news_list': news_list, 'selected_city': city})


# def category_filter(request, category):
#     city = request.GET.get('city', '')
#     print("Selected city:", city)
#     # Ваша логика фильтрации новостей
#     news_list = News.objects.filter(category=category, city=city)  # Фильтруем новости по категории и городу
#     return render(request, 'filtered_news.html', {'news_list': news_list, 'selected_city': city})
#
# def category_filter(request, category):
#     city = request.GET.get('city')  # Получение значения city из запроса
#     if city:
#         news = News.objects.filter(city=city)
#     else:
#         news = News.objects.all()
#     return render(request, 'filtered_news.html', {'news': news, 'selected_city': city})


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


from django.http import JsonResponse
from .models import News

def track_news_view(request, title):
    try:
        news = News.objects.get(title=title)
        news.views += 1
        news.save()
        return JsonResponse({'success': True})
    except News.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'News not found'}, status=404)



def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news
                comment.user = request.user
                comment.save()
                # После добавления комментария перенаправляем обратно на страницу всех новостей
                return redirect('all_news')
        else:
            # Если пользователь не авторизован, перенаправляем его на страницу входа
            return redirect('login')
    else:
        form = CommentForm()
    return render(request, 'all_news.html', {'news': news, 'comments': comments, 'form': form})

from django.shortcuts import redirect
from .models import News, Comment

def add_comment(request, pk):
    if request.method == 'POST':
        text = request.POST.get('text')
        news = News.objects.get(pk=pk)
        Comment.objects.create(news=news, author=request.user, text=text)
    return redirect('all_news')  # Перенаправление на страницу всех новостей