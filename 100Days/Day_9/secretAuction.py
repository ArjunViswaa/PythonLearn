import art

isAnotherUser = True
bids = {}

print(art.logo)

def find_highest_bidder(bidding_dict) : 
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict : 
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid : 
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of $ {highest_bid}")

while isAnotherUser : 
    name = input("What is your name ? ")
    price = int(input("What is your bid ? In $"))

    bids[name] = price
    should_continue = input("Are there any other bidders ? Type 'yes' or 'no'. \n").lower()
    if(should_continue == "no") : 
        isAnotherUser = False
        find_highest_bidder(bids)
    elif should_continue == "yes" : 
        print("\n" * 100)