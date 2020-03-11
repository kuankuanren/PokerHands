import poker
import pytest
def test_IsFlush():
    assert poker.pokerHand("2H 3H 4H 5H 6H").IsFlush()== 1
def test_IsStraight():
    assert poker.pokerHand("2H 3H 4H 5H 6H").IsStraight() == 1

def test_compare():
    hand,other = "2H 3H 4H 5H 6H" , "KS AS TS QS JS"
    player, opponent = poker.pokerHand(hand), poker.pokerHand(other)
    assert(player.compare_with(opponent) == "white wins")


