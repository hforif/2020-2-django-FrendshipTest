from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('complete/', views.complete, name="complete"),
    path('player_home/<int:pk>/', views.player_home, name='player_home'),
    path('result/<int:pk>/', views.result, name='result'),
    path('master_home', views.master_home, name="master_home"),
]