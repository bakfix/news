from django.urls import path
from .views import NewsListCreateView, NewsRetrieveUpdateDestroyView, AllNewsListView
from . import views
from .views import subscribe

urlpatterns = [
    path('', AllNewsListView.as_view(), name='all_news'),
    path('news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('login/', views.login_view, name='login'),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroyView.as_view(), name='news-retrieve-update-destroy'),
    path('register/', views.register_view, name='welcome '),  # Измененный URL-шаблон для отображения всех новостей
    path('subscribe/', subscribe, name='subscribe'),  # URL-маршрут для представления subscribe
]
