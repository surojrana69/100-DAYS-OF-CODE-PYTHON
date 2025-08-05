import random
from art import logo


def deal_card():
    """
    Returns a random card from the deck.
    The deck contains values representing cards in Blackjack.
    11 is used for Ace, which can also be 1 if needed.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Calculates the score of a hand (list of cards).
    Returns:
    - 0 if the hand is a Blackjack (2 cards that sum to 21).
    - Converts Ace (11) to 1 if the score is over 21.
    - Otherwise, returns the sum of the cards.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """
    Compares the user's score and the computer's score and returns the result.

    Parameters:
    - u_score: int - user’s final score
    - c_score: int - computer’s final score

    Returns:
    - A string describing the game outcome: win, lose, draw, or Blackjack.
    """
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """
    Runs one round of Blackjack game between user and computer.
    Handles dealing cards, checking scores, user input for drawing more cards,
    and determining the winner.
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial two cards for both user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for end conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws until score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Start the game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # Clear screen
    play_game()
