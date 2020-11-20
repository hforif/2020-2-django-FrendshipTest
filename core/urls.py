from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:pk>/choice1', views.result, name="result"),
    path('<int:pk>/choice2', views.result, name="choice2"),
    path('<int:pk>/choice3', views.result, name="choice3"),
    path('<int:pk>/choice4', views.result, name="choice4"),
    path('<int:pk>/choice5', views.result, name="choice5"),
    path('<int:pk>/choice6', views.result, name="choice6"),
    path('<int:pk>/choice7', views.result, name="choice7"),
    path('<int:pk>/choice8', views.result, name="choice8"),
    path('<int:pk>/choice9', views.result, name="choice9"),
    path('<int:pk>/choice10', views.result, name="choice10"),

    path('<int:pk>/choice11', views.result2, name="result2"),
    path('<int:pk>/choice22', views.result2, name="choice2"),
    path('<int:pk>/choice33', views.result2, name="choice3"),
    path('<int:pk>/choice44', views.result2, name="choice4"),
    path('<int:pk>/choice55', views.result2, name="choice5"),
    path('<int:pk>/choice66', views.result2, name="choice6"),
    path('<int:pk>/choice77', views.result2, name="choice7"),
    path('<int:pk>/choice88', views.result2, name="choice8"),
    path('<int:pk>/choice99', views.result2, name="choice9"),
    path('<int:pk>/choice100', views.result2, name="choice10"),
    
    path('complete/', views.complete, name="complete"),
    path('player_home/<int:pk>/', views.player_home, name='player_home'),
    path('result/<int:pk>/', views.result_, name='result_'),
    path('master_home', views.master_home, name="master_home"),
    path('', views.start, name="start"),
]