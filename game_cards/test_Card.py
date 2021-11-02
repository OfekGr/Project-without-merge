from unittest import TestCase


class TestCard(TestCase):
    #If it receives more than 2 values
    def test_init_(self):
        raise AssertionError("Only 2 values allowed: card value and card suit")

    # Check if card is not an integer
    def test_check_sign(self):
        if type(self.value) != int or type(self.suit):
            raise AssertionError("Card type is not a number")

