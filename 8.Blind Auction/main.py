# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added}
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a highest bid of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Would you like to continue? (y/n): ")
    if should_continue == "y":
        print("\n" * 20)
    elif should_continue == "n":
        continue_bidding = False
        find_highest_bidder(bids)