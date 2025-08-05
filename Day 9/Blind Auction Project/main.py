# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner= bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}.")


bid={}
should_continue=True
while should_continue:
    name = input("Enter your name:")
    price = int(input("Enter your bid: $"))
    bid [name] = price
    any_other = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if any_other == "no":
        should_continue=False
        find_highest_bidder(bid)
    elif should_continue == "yes":
        print("\n"*50)