hammer = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(hammer)
c = ""
bids = {}
repeat = True

while repeat:
    name = input("Enter name : ")
    bid = int(input("Enter bid $ : "))
    bids[name] = bid

    c = input("\nadd more bids? y/n")
    if c == "y":
        repeat = True
    else:
        repeat = False

highesh = 0
for bidder in bids:
    amount = bids[bidder]
    if amount > highesh:
        highesh = amount
        winner = bidder

print(f"\n\nWinner is {winner}\nHighest Bid = ${highesh}")
