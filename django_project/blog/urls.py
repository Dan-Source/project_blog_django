from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path(
        'user/<str:username>', views.UserPostListView.as_view(),
        name='user-posts'
    ),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreatedView.as_view(), name='post-create'),
    path(
        'post/<int:pk>/update/', views.PostUpdateView.as_view(),
        name='post-update'
    ),
    path(
        'post/<int:pk>/delete/', views.PostDeleteView.as_view(),
        name='post-delete'
    ),
    path('about/', views.about, name='blog-about'),
    
    path('api/v1/', include(router.urls))
]
