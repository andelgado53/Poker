from random import shuffle
from pprint import pprint

def extract_rank_from_card(card):
    """
    >>> extract_rank_from_card("8C")
    >>> 8
    >>> extract_rank_from_card("KC")
    >>> 13
    """
    face_card_ranks = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    rank = card[0]
    return int(face_card_ranks.get(rank, rank))

def extract_suite_from_card(card):
    return card[1]

def card_ranks(hand):
    """
    >>> card_ranks(["6C", "7C", "8C", "9C", "TC"])
    >>> (10, 9, 8, 7, 6)
    """
    ranks = sorted([extract_rank_from_card(card) for card in hand], reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        return (5, 4, 3, 2, 1)
    return tuple(ranks)

def straight(ranks):
    unique_ranks = set(ranks)
    if max(ranks) - min(ranks) == 4 and len(unique_ranks) == 5:
        return True
    return False

def flush(hand):
    return len(set([extract_suite_from_card(card) for card in hand])) == 1

def kind(num_of_cards, ranks):
    ns = ["-", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if num_of_cards <= 0:
        return None
    for r in ranks:
        ns[r] = ns[r] + 1
    index = len(ns) - 1
    while index >= 0:
        if ns[index] == num_of_cards:
            return index
        index -= 1
    return None

def two_pair(ranks):
    """
    >>> two_pair((6,6,5,5,2))
    >>> (6,5)
    >>> two_pair((10, 9,9, 8,8))
    >>> (9,8)
    >>> two_pair((9,9,8,7,7))
    >>> (9,7)
    """
    high = kind(2, ranks)
    if high is None:
        return high
    low = kind(2, [r for r in ranks if r != high])
    if low is None:
        return low
    return (high, low)
    
def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    max_value = max(iterable, key=key)
    # print(max_value)
    return [hand for hand in iterable if key(hand) == key(max_value)]

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, max(ranks),ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks),ranks)
    else:                                          # high card
        return (0, ranks)

def convert_rank_to_hand_name(handRank):
    rank = handRank[0]
    if rank == 8:
        return "straight fush"
    elif rank == 7:
        return "4 of a kind"
    elif rank == 6:
        return "full house"
    elif rank == 5:
        return "flush"
    elif rank == 4:
        return "straight"
    elif rank == 3:
        return "3 of a kind"
    elif rank == 2:
        return "two pair"
    elif rank == 1:
        return "one pair"
    else:
        return "high card"

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    ls = "AD 3H 2C 4D 5H".split()
    hs = "TH JC QD KC AH".split()
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert straight([9, 8, 8, 6, 5]) == False
    assert straight([5, 4, 3,2, 1]) == True
    assert straight(card_ranks(ls)) == True
    assert straight(card_ranks(hs)) == True
    assert hand_rank(ls) == (4,5)
    return 'tests pass'
    

# test()

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    hands = []
    current_hand = []
    shuffle(deck)
    for hand in range(numhands):
        current_hand = deck[n*hand:n*hand+5]
        hands.append(current_hand)
        current_hand = []
    return hands


# c = deal(3)
# print(c)
# print(poker(c))



# print(poker([['4D', 'TS', '6C', '3S', 'KH'], ['JS', '5S', 'AD', '9S', '5H'], ['QC', 'AH', '2D', '3D', 'AS']]))

# hands = [['4D', 'TS', '6C', '3S', 'KH'], ['JS', '5S', 'AD', '9S', '5H'], ['QC', 'AH', '2D', '3D', 'AS']]

# for hand in hands:
#     print(hand_rank(hand))
# print(hand_rank(['2H', 'AS', '6S', 'KS', 'AD']))
# print(hand_rank(['KH', '7D', 'QC', 'JH', '2S']))


