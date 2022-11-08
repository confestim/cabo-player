import random

# Deck generation
names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
specials = ["peek", "swap", "draw"]

def create_deck():
    deck = []
    for s in suits:
        for v in names:
            deck.append((v, s))
    return deck

deck = create_deck()

# Check for special card
def special_card(card):
    if card[0] == "9" or card[0] == "10":
        return "peek"
    elif card[0] == "Jack" or card[0] == "Queen":
        return "swap"
    elif card[0] == "King":
        return "draw"
    else:
        return card[0]

# Draw a card
def get_card():
    try:
        card = random.choice(deck)
        deck.remove(card)
        return special_card(card)
    except IndexError:
        raise Exception("End of deck")

# Player class
class Player:
    # Get player hands
    def __init__(self):
        self.idx = 1
        self.cards = {}
        for i in range(4):
            self.cards[i] = get_card()
        print("Left: " + self.cards[0] + " Right: " + self.cards[3])

    # Take a peek at something you haven't before(not quite)
    # ^^^ TODO: Do what the comment says ^^^
    def peek(self):
        print(self.cards[self.idx])
        self.idx += 1
        if self.idx > 3:
            self.idx = 0

# Do stuff in case of card draws
def check(drawn, player):
    # TODO: Add all special cases
    if drawn in specials:
        if drawn == "peek":
            player.peek()
    # NOTE: Maybe we should disregard this basic strategy and try to implement the rules of the game better
    else:
        if drawn < player.cards[0] or (player.cards[0] in specials and drawn not in specials):
            player.cards[0] = drawn
        elif drawn < player.cards[3] or (player.cards[3] in specials and drawn not in specials):
            player.cards[3] = drawn
        else:
            player.cards[random.randint(1, 2)] = drawn

def main():
    # Simulation
    from time import sleep
    p1 = Player()
    p2 = Player()
    while True:

        print(p1.cards)
        drawn = get_card()
        print(f"{drawn} is drawn for Player 1")
        check(drawn, p1)

        print(p2.cards)
        drawn = get_card()
        print(f"{drawn} is drawn for Player 2")
        check(drawn, p2)

        sleep(.5)

if __name__ == "__main__":
    main()



