import random
from colorama import Fore, Back, Style

loser = Fore.BLACK + Back.RED + Style.BRIGHT
winner = Fore.BLACK + Back.GREEN + Style.BRIGHT


def is_win(player, opponent):
    # returns true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


def play():
    user = input("Let's play Rock, Paper, Scissors.  \nWhat do you choose? Rock(r), Paper(p), Scissors(s): ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie!'

    if is_win(user, computer):
        return 'Congratulations, you have won!. Your opponent chose ' + winner + str(computer)

    return 'I am sorry you have lost.  Your opponent chose ' + loser + str(computer)


print(play())
