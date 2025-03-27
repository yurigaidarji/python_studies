import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def first_draw(user_deck, dealer_deck):
    for _ in range(2):
        user_deck.append(deal_card())
        dealer_deck.append(deal_card())

def calculate_score(cards):
    #Black jack will be 0 in our game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare_scores(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "You lost, dealer got a Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over 21, you lose"
    elif dealer_score > 21:
        return "Dealer went over 21, you win"
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You lose"
    

def play_game():
    user_hand = []
    dealer_hand = []
    is_end_game = False
    print(logo)

    first_draw(user_hand, dealer_hand)

    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)

    while not is_end_game:
        print(f"User cards: {user_hand}, user score: {user_score}")
        print(f"Dealer first card: {dealer_hand[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_end_game = True
        else:
            user_draw_decision = input("Type 'y' to get another card, or 'n' to pass: ")
            if user_draw_decision == 'y':
                user_hand.append(deal_card())
                user_score = calculate_score(user_hand)
            else:
                is_end_game = True

    #Dealer's turn
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"User's hand: {user_hand}")
    print(f"Dealer's hand: {dealer_hand}")
    print(compare_scores(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()