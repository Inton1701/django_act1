from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_rps, name='start_rps'), 
    path('game_rps/', views.game_rps, name='game_rps'), 
    path('check_rps/', views.check_result, name='check_result'), 
   path('result_rps/<str:result>/<str:computer_choice>/<str:player_choice>/', views.result_rps, name='result_rps'),
    path('quit_rps/', views.quit_game, name='quit_game'),  
]