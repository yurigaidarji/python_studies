# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)

new_users = True
bids = {}

while new_users:
    user_name = input("What is your name? ")
    user_bid = float(input("What is your bid? $"))
    bids[user_name] = user_bid

    if input("Are there new bidders? ('y' or 'n'): ") == "n":
        new_users = False

print(bids)

def get_highest_bid (bids_dictionary):

    highest_bid = 0.0
    for bidder in bids_dictionary:
        bid = bids_dictionary[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    return winner

print(get_highest_bid(bids))
