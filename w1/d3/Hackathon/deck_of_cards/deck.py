from card import Card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                pointval = i
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                    pointval = 10
                elif i == 12:
                    str_val = "Queen"
                    pointval = 10
                elif i == 13:
                    str_val = "King"
                    pointval = 10
                else:
                    str_val = str(i)
                self.cards.append( Card( s , pointval , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def black_jack(self):
        self.shuffle()
        print("Your cards: ")
        print(self.cards[0].card_info(), self.cards[2].card_info())
        points = 0
        dpoints = 0
        points += self.cards[0].point_val
        dpoints += self.cards[1].point_val
        points += self.cards[2].point_val
        dpoints += self.cards[3].point_val
        print(f"dealer has: {dpoints} points")
        if points > 21:
            print("Bust!")
        elif dpoints > 21:
            print("Dealer bust!")
        elif dpoints == 21:
            print("Dealer blackjack")
        elif points == 21:
            print("Blackjack!")
        elif points and dpoints < 21:
            num = 4
            while points and dpoints < 21:
                if points < 21:
                    choice = input("Hit or Stay?")
                    if choice == "hit":
                            print(self.cards[num].card_info())
                            points += self.cards[num].point_val
                    elif choice == "stay":
                        print(f"Stayed at {points} points.")
                        num1 = num + 2
                        while dpoints < 17:
                            print("dealer hits:")
                            print(self.cards[num1].card_info())
                            dpoints += self.cards[num1].point_val
                            num1+=1
                        print(f"dealer stays at {dpoints} points")
                        break
                else:
                    break
                num+=2
            if points > 21:
                print("Bust!")
            elif dpoints > 21:
                print("Dealer bust!")
            elif dpoints == 21:
                print("Dealer blackjack!")
            elif points == 21:
                print("Blackjack!")
            else:
                if points > dpoints:
                    print("You won!")
                elif points == dpoints:
                    print("Tie, dealer wins!")
                elif points < dpoints:
                    print("You lose!")
        return self