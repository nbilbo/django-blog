from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path(
        'posts/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post-detail',
    ),
    path('api/', views.api_view, name='api-view'),
    path('api/posts/', views.PostListApi.as_view(), name='post-list-api'),
    path(
        'api/posts/<int:pk>/',
        views.PostDetailApi.as_view(),
        name='post-detail-api',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
