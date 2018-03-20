import Poker

hand_winners = {}
deals = 100000

for deal in range(deals):
    hands = Poker.deal(numhands=10)
    for hand in hands:
        key = Poker.convert_rank_to_hand_name(Poker.hand_rank(hand))
        hand_winners[key] = hand_winners.get(key, 0) + 1

def reverse_tuple(entry):
     return (entry[1], entry[0])


for hand in sorted(hand_winners.items(), key=reverse_tuple, reverse=True):
    print(hand[0] + ": " + str(hand[1]) + " percentage " + str((hand[1]*1.0/ deals*10)))