def bid_input(name_input, price_input):
    bid_list.append({
        "name_bidder" : name_input,
        "price_bid" : price_input
    })
    
def bid_result():
    y = 0
    price_total = 0
    for x in bid_list:
        if bid_list[y]["price_bid"] > price_total: 
            price_total = bid_list[y]["price_bid"]
            bid_winner = bid_list[y]
            # print(bid_list[y])
        y += 1
    print(bid_winner)
    

condition = True
bid_list = []
bid_winner = {}

while condition:
    name = input("What is the name of the bidder? ")
    price = int(input("What is the price of bid? "))
    bid_input(name_input = name , price_input = price)
    print(bid_list)

    condition_input = input("Is there any other bidder? type yes or no. ")
    if condition_input == "no":
        condition = False
bid_result()