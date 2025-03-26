import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)
user_hand = []
dealer_hand = []
end_game = False

while not end_game:
    user_hand.append(random.randint(0,12))
    user_hand.append(random.randint(0,12))
    dealer_hand.append(random.randint(0,12))
    dealer_hand.append(random.randint(0,12))
    user_score = user_hand[0] + user_hand[1]
    dealer_score = dealer_hand[0] + dealer_hand[1]

    print(f"Your cards: [{user_hand[0]}, {user_hand[1]}], current score {user_score}")
    print(f"Computer's first card: {dealer_hand[0]}")

    if user_score == 21:
        print("You win!")
        end_game = True
    elif user_score > 21:
        print("You loose!")
        end_game = True

    if not end_game:
        user_decision = input("Type 'y' to get another card, or 'n' to pass: ")

        if user_decision == 'y':
            keep_drawing = True
        else:
            keep_drawing = False

        while keep_drawing:
            new_card = random.randint(0, 12)
            user_score += new_card
            user_hand.append(new_card)

            if user_score == 21:
                print("You win!")
                end_game = True
                keep_drawing = False
            elif user_score > 21:
                print("You loose!")
                end_game = True
                keep_drawing = False

            print(f"Your cards: [")
            for card in user_hand:
                print(f"{card}, ")
            print(f"], current score {user_score}")

            if not end_game:
                user_decision = input("Type 'y' to get another card, or 'n' to pass: ")

                if user_decision == 'y':
                    keep_drawing = True
                else:
                    keep_drawing = False

        dealer_draw = False
        if dealer_score < 16:
            dealer_draw = True

        while dealer_draw and not end_game:
            new_card = random.randint(0, 12)
            dealer_score += new_card
            dealer_hand.append(new_card)

            if dealer_score > 21:
                print(f"You win, your final score was {user_score}, and computers score was {dealer_score}")
                end_game = True
                dealer_draw = False
            elif dealer_score >= 16 and dealer_score < user_score:
                dealer_draw = True


        if user_score > dealer_score and not end_game:
            print(f"You win, your final score was {user_score}, and computers score was {dealer_score}")
            end_game = True
        elif user_score == dealer_score and not end_game:
            print(f"Draw, both got {user_score}")
            end_game = True
        elif not end_game:
            print(f"You loose, your final score was {user_score}, and computers score was {dealer_score}")
            end_game = True