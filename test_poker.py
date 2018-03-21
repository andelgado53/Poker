from unittest import TestCase
import unittest
import Poker

class TestPoker(TestCase):

    def setUp(self):
        self.sf = "6C 7C 8C 9C TC".split() # Straight Flush
        self.fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
        self.fh = "TD TC TH 7C 7D".split() # Full House
        self.flush = "AH 7H 3H TH 2H".split() # Flush
        self.lows = "AD 3H 2C 4D 5H".split() # Straight 
        self.highs = "TH JC QD KC AH".split() # Straight
        self.two_pair = "AD AH 3H 3D JS".split() # two pair
        self.one_pair = "2H 2D AC 8H 9H".split() # one pair
        self.high_card = "8H 3S 7H 4D TD".split() # high card


    def test_extract_rank_from_card(self):
        self.assertEqual(Poker.extract_rank_from_card("TC"), 10)
        self.assertEqual(Poker.extract_rank_from_card("JC"), 11)
        self.assertEqual(Poker.extract_rank_from_card("QC"), 12)
        self.assertEqual(Poker.extract_rank_from_card("KC"), 13)
        self.assertEqual(Poker.extract_rank_from_card("AC"), 14)
        self.assertEqual(Poker.extract_rank_from_card("9C"), 9)
        self.assertEqual(Poker.extract_rank_from_card("2C"), 2)
    
    def test_extract_suite_from_card(self):
        self.assertEqual(Poker.extract_suite_from_card("TC"), "C")
        self.assertEqual(Poker.extract_suite_from_card("TH"), "H")
    
    def test_card_ranks(self):
        self.assertEqual(Poker.card_ranks("6C 7C 8C 9C TC".split()), (10, 9, 8, 7, 6))
        self.assertEqual(Poker.card_ranks("9D 9H 9S 9C 7D".split()), (9, 9, 9, 9, 7))
        self.assertEqual(Poker.card_ranks("TD TC TH 7C 7D".split()), (10, 10, 10, 7, 7))
        self.assertEqual(Poker.card_ranks("AH 7H 3H TH 2H".split()), (14, 10, 7, 3, 2))
        self.assertEqual(Poker.card_ranks("AD 3H 2C 4D 5H".split()), (5, 4, 3, 2, 1))
        self.assertEqual(Poker.card_ranks("TH JC QD KC AH".split()), (14, 13, 12, 11, 10))
        self.assertEqual(Poker.card_ranks("AD AH 3H 3D JS".split()), (14, 14, 11, 3, 3))
        self.assertEqual(Poker.card_ranks("2H 2D AC 8H 9H".split()), (14, 9, 8, 2, 2))
        self.assertEqual(Poker.card_ranks("8H 3S 7H 4D TD".split()), (10, 8, 7, 4, 3))

    def test_straight(self):
        self.assertTrue(Poker.straight((14, 13, 12, 11, 10)))
        self.assertTrue(Poker.straight((5, 4, 3, 2, 1)))
        self.assertTrue(Poker.straight((10, 9, 8, 7, 6)))
        self.assertFalse(Poker.straight((10, 8, 7, 4, 3)))
    
    def test_flush(self):
        self.assertTrue(Poker.flush("6C 7C 8C 9C TC".split()))
        self.assertTrue(Poker.flush("AH 7H 3H TH 2H".split()))
        self.assertFalse(Poker.flush("2H 2D AC 8H 9H".split()))
    
    def test_kind(self):
        self.assertEqual(Poker.kind(4, (10, 10, 10, 10, 6)), 10)
        self.assertIsNone(Poker.kind(4, (10, 10, 10, 6, 2)))
        self.assertEqual(Poker.kind(3, (10, 10, 10, 6, 2)), 10)
        self.assertEqual(Poker.kind(2, (10, 10, 9, 6, 2)), 10)
        self.assertEqual(Poker.kind(1, (10, 9, 8, 6, 2)), 10)
        self.assertIsNone(Poker.kind(0, (10, 9, 8, 6, 2)))
        self.assertIsNone(Poker.kind(-5, (10, 9, 8, 6, 2)))






        
if __name__ == '__main__':
    unittest.main()