"""
-------------------------------------------------------------------------------
Name:		Coin.py
Purpose:
Simulates a coin flip

Author:		Fabroa.E

Created:		22/03/2019
------------------------------------------------------------------------------
"""

import random

class Coin(object):
    """
    Models a coin as an object
    """

    def __init__(self):
        """
        Initializes the face of the coin to either heads or tails
        :return: None
        """

        self.face = random.choice(["heads", "tails"])


    def get_face(self):
        """
        Retrieves the current face of the coin facing up
        :return: string The value of the face attribute
        """
        return self.face

    def flip(self):
        """
        Sets the face attribute to heads or tails
        :return: None
        """
        self.face = random.choice(["heads", "tails"])



# Simulates 1000 coin flips and saves the data to accumulator variables
if __name__ == '__main__':

    # initialize the counters
    heads = 0
    tails = 0

    for i in range(1000):
        myCoin = Coin()
        myCoin.flip()

        if myCoin.get_face() == "heads":
            heads += 1
        else:
            tails += 1

    print("Total Heads: " + str(heads) + "\nTotal Tails: " + str(tails))