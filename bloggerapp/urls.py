from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from bloggerapp import views



urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('profile/edit/', views.edit_profile, name = 'edit'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.post_list, name='post_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('posts/create/', views.create_post, name='create_post'),
    path('profile/', views.view_profile, name = 'view_profile'),
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('logout/', views.logout_user, name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)