import Poker

my_hand = ["AS", "AH", "3D", "TC", "8C"]
my_set_hand = set(my_hand)
rest_of_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC' if r+s not in my_set_hand] 

wins = [0,0]
hand_winners = {}
deals = 10000
for deal in range(deals):
    hands = Poker.deal(numhands=8, n=5, deck=rest_of_deck) 
    hands.append(my_hand)
    winners = Poker.poker(hands)
    if my_hand in winners:
        wins[0] += 1
    else:
        wins[1] += 1
    
    for winer in winners:
        key = Poker.convert_rank_to_hand_name(Poker.hand_rank(winer))
        hand_winners[key] = hand_winners.get(key, 0) + 1

def reverse_tuple(entry):
     return (entry[1], entry[0])
print(wins)
print(hand_winners)

for hand in sorted(hand_winners.items(), key=reverse_tuple, reverse=True):
    print(hand[0] + ": " + str(hand[1]) + " percentage " + str((hand[1]*1.0/ deals)))