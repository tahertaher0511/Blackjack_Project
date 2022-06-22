from os import system, name
import random
from art import logo


def clear():
    """This function will clear the screen to start over new game. Then whenever you want to clear the screen,
    just use this clear function Then go for main.py and modify the  configuration to and checks the box if imulate
    terminal in output console is activate.
    """
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system("cls")
    # and for mac and linux, the os.name is "posix"
    else:
        _ = system("clear")


play_game = True


def blackjack_game():
    global user_score, computer_score
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    is_game_over = False

    def deal_card():
        """Returns a card form a deck randomly."""
        card = random.choice(cards)
        return card

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(list_of_cards):
        """Takes a list of cards as input and calculate the sum of score."""
        if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
            return 0  # Check is user or computer has a Blackjack == 21
        if 11 in list_of_cards and sum(list_of_cards) > 21:
            # Check if User or Computer has a Blackjack
            # ('Ace'11, 10), 0 will represent a Blackjack in our game.
            list_of_cards.remove(11)
            list_of_cards.append(1)
        return sum(list_of_cards)

    def compare(user_scores, computer_scores):
        if user_scores == computer_scores:
            return "Draw!"
        elif computer_scores == 0:
            return "you lose, the opponent has a Blackjack!"
        elif user_scores == 0:
            return "You win, with a Blackjack!"
        elif user_scores > 21:
            return "You lose, you went over!"
        elif computer_scores > 21:
            return "Opponent went over, you win!"
        elif user_scores > computer_scores:
            return "You win!"
        else:
            return "You lose!"

    while not is_game_over:
        """This logic is for user to calculate it progress in this game."""
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}.")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            ask_user_for_another_card = input("Type 'y' to get another card or type 'n' to pass.").lower()
            if ask_user_for_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Final score: {user_score}.")
    print(f"Computer final hand: {computer_cards}, Final score: {computer_score}")
    print(compare(user_score, computer_score))


while play_game:
    play = input(f"Do you want to play a game of a Blackjack? Type 'y' or 'n' for exit: ").lower()
    clear()
    if play == "y":
        print(logo)
        blackjack_game()
    else:
        print("Bye bye, Hopefully you enjoy it.")
