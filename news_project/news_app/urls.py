from django.urls import path
from .views import NewsListCreateView, NewsRetrieveUpdateDestroyView, AllNewsListView, news_by_city, track_news_view
from . import views
from .views import subscribe
from .views import all_news_view, category_filter_view

urlpatterns = [
    path('', news_by_city, name='all_news'),
    path('news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('login/', views.login_view, name='login'),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroyView.as_view(), name='news-retrieve-update-destroy'),
    path('subscribe/register/', views.register_view, name='welcome '),  # Измененный URL-шаблон для отображения всех новостей
    path('subscribe/', subscribe, name='subscribe'),  # URL-маршрут для представления subscribe
    path('category/<str:category>/', views.category_filter_view, name='category_filter_view'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('news_by_city/', news_by_city, name='news_by_city'),
    path('track-news-view/<str:title>/', track_news_view, name='track_news_view'),
    path('news/<int:pk>/comment/', views.add_comment, name='add_comment'),
]
