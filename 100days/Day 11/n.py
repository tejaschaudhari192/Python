import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
gameover=False

def cards():
    '''Returns a random card from cat'''
    cat = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cat)
    return card

pcards=[]
ccards=[]

for c in range(2):
    pcards.append(cards())
    ccards.append(cards())

print(pcards)
print(ccards)

def score(chosen_cards):
    """returns total score of chosen cards"""
    if sum(chosen_cards)==21 and len(chosen_cards)==2:
        return 0
    
    if 11 in chosen_cards and sum(chosen_cards)>21:
        chosen_cards.remove(11)
        chosen_cards.append(1)
        
    return sum(chosen_cards)

cscore= score(pcards)
pscore= score(ccards)

if cscore==0 or pscore==0 or cscore>21 or pscore>21 :
    gameover=True