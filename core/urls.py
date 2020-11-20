from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('<int:pk>/choice2', views.result, name="choice2"),
    path('<int:pk>/choice3', views.result, name="choice3"),
    path('<int:pk>/choice4', views.result, name="choice4"),
    path('<int:pk>/choice5', views.result, name="choice5"),
    path('<int:pk>/choice6', views.result, name="choice6"),
    path('<int:pk>/choice7', views.result, name="choice7"),
    path('<int:pk>/choice8', views.result, name="choice8"),
    path('<int:pk>/choice9', views.result, name="choice9"),
    path('<int:pk>/choice10', views.result, name="choice10"),
    
]