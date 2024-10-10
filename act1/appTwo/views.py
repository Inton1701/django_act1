from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import random

def start_rps(request):
    return render(request,'start_rps.html')
def game_rps(request):

    return render(request,'game_rps.html')

def check_result(request):
    choices = random.choice(['rock','paper','scissors'])
    player_hand = request.POST['player_hand']
    robot_hand = choices

    #check if equal
    if player_hand == robot_hand:
        return redirect('result_rps', result='Draw!',  computer_choice=robot_hand, player_choice=player_hand)
    
    # Determine if player wins
    if (player_hand == 'rock' and robot_hand == 'scissors') or \
       (player_hand == 'paper' and robot_hand == 'rock') or \
       (player_hand == 'scissors' and robot_hand == 'paper'):
        return redirect('result_rps', result='You win!', computer_choice=robot_hand, player_choice=player_hand)
    
    # Otherwise, player loses
    return redirect('result_rps', result='You lose!',  computer_choice=robot_hand, player_choice=player_hand)
def result_rps(request,result,computer_choice,player_choice):
   return render(request, 'result_rps.html', {'result': result, 'computer_choice': computer_choice, 'player_choice': player_choice})

def quit_game(request):
    # destroy the session
    request.session.flush()
    # redirect to start page
    return redirect('start_rps')

# Create your views here.
