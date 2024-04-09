from django.contrib.auth import authenticate, login
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

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
