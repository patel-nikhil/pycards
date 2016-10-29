from cardsets import CSI

#Klondike layout

class CardGame:
    pass
    #type
    #name
    #numcards
    #

    #numRows
    #row: position  base    alternate   direction

    #

from pile import Pile
from stack import Stack


class Klondike(CardGame):

    def __init__(self):
        self.type = CSI.TYPE_FRENCH
        self.name = Klondike
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 7
        self.numcards = 52
        self.foundations = 4

    # Pile(pos, base, alternate, direction, size)
    def createPiles(self):
        self.piles = []
        self.piles.append(Pile((50, 50), -1, [], None, 24))
        self.piles.append(Pile((100 + 50, 50), -1, [], None, 0))
        for p in range(self.foundations):
            self.piles.append(Pile(((self.numrows-p+1) * 80 + 10, 50), 1, 1, False, 0)) # create foundation piles
        for p in range(self.numrows):
            self.piles.append(Pile((p*100+50,250), 13, -1, True, p)) # create normal piles

    # Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def createStacks(self):
        self.deckID = 0
        self.wasteID = 1
        self.stacks.append(Stack(0, 50, 50, -1, False, 0, [-1]*24, False, deck=True)) # Deck
        self.stacks.append(Stack(1, 100 + 50, 50, -1, False, 0, [], False))  # Waste

        stackCount = 2
        for num in range(self.foundations):
            _x = (self.numrows - num + 1) * 80 + 10
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, 1, False, 1, [], True, sameSuit=True)) # create foundation stacks
            stackCount += 1

        for num in range(self.numrows):
            _x = num * 100 + 50
            _y = 250

            def cards():
                if num == 0:
                    return [1]
                else:
                    return [-1]*(num) + [1]

            self.stacks.append(Stack(stackCount, _x, _y, 13, True, -1, cards(),offset=15))  # create normal stacks
            stackCount += 1

    def deal(self):
        print len (k.stacks[self.deckID].cards)
        for i in range(1, 4):
            card = k.stacks[self.deckID].cards[-i]
            cardImg = k.stacks[self.deckID].cardWidgets[-i]
            k.stacks[self.deckID].cards.pop()
            k.stacks[self.wasteID].cards.append(card)
            k.stacks[self.deckID].cardWidgets.pop()
            k.stacks[self.wasteID].cardWidgets.append(cardImg)
        for cardImg in k.stacks[self.wasteID].cardWidgets:
            cardImg.place(x=k.stacks[self.wasteID].x,
                y=k.stacks[self.wasteID].y + \
                    cardImg.cardNum * k.stacks[self.wasteID].offset)
        card = k.stacks[self.deckID].cardWidgets[-1]
        card.place(
            x=k.stacks[self.deckID].x,
            y=k.stacks[self.deckID].y + \
              card.cardNum * k.stacks[self.deckID].offset)
        print card.rank, card.suit

k = Klondike()
k.createPiles()
k.createStacks()