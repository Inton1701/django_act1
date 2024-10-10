from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'), 
    path('guess/', views.guess_number, name='guess_number'), 
    path('result/<str:result>/', views.result_page, name='result_page'),
    path('quit/', views.quit_game, name='quit_game'),  
]
