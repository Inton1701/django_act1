from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import random
def start_game(request):
    #generate random num and set to session
    request.session['secret_number'] = random.randint(1, 100)
    request.session['attempts'] = 5
    #redirect to game_page after clicking the start game
    return render(request, 'start_game.html')

def guess_number(request):

    # get the secret number and attempt from the session and
    secret_number = request.session.get('secret_number')
    attempts = request.session.get('attempts', 5)

    if request.method == 'POST':
        guess = int(request.POST['guess'])
        attempts -= 1  

        request.session['attempts'] = attempts

        if guess < secret_number:
            message = "Too low!"
        elif guess > secret_number:
            message = "Too high!"
        else:
            return redirect('result_page', result='win')

        if attempts <= 0:
            return redirect('result_page', result='lose')

        # return message if number is low or high and the atttempt count
        return render(request, 'game_page.html', {'message': message, 'attempts_left': attempts})

    return render(request, 'game_page.html', {'attempts_left': attempts})
def play_game(request):
    # redirect to start game page
    return render('game_page.html')

def quit_game(request):
    # destroy the session
    request.session.flush()
    # redirect to start page
    return redirect('start_game')
def result_page(request, result):
    # get secret number from session and show to result page
    secret_number = request.session.get('secret_number')
    if result == 'win':
        result_title = "Congratulations, You Won!"
        result_message = f"You guessed the number {secret_number} correctly!"
    else:
        result_title = "Sorry, You Lost!"
        result_message = f"The correct number was {secret_number}."

    # destroyu the sessoin
    request.session.flush()
    # redirect to result page to display the result
    return render(request, 'result_page.html', {
        'result_title': result_title,
        'result_message': result_message
    })
