import random 
import this
"""
Poker hands: https://www.cardplayer.com/rules-of-poker/hand-rankings


"""

# Init - setting up the basic values of each card, value, 
#suit, name, showing: que tem a intenção de mostrar para o usuário quando solicitado a sua carta
class Card( object ):
    def __init__(self, name,value, suit):
        self.value = value
        self.suit = suit
        self.name = name
        self.showing = False 
        
    #def é utilizado para representar o objeto. Serve para mostrar customizar o que retorna - para saber o status de uma ação.
    
    def __repr__(self):
        if self.showing:#se a funcao showing for chamada a pessoa vera as cartas na sua mao
            return str(self.name) + " of " + self.suit #retorna os valores da sua carta.
        else: "Card" #quando a pessoa recebe a carta ela ja recebe a mensagem automática que recebeu uma carta aleatória, representa a 'back of a card'

class Deck(object):
    # it randomizes the order of items in a list, we call it a randomizes the elements of a list in place
    def shuffle(self, times = 1):
        random.shuffle(self.cards)
        print("Deck Shuffle")
        
    def deal(self):
        return self.pop(-1)
    #The pop() method removes the item at the given index from the list and returns the removed item.
    #pop utilizei para pegar a última carta do deck
    
    #standard deck está criando o deck de cartas
    
class StandardDeck(Deck):
    def __init__(self):
        self.cards = []
        suits = ["Hearts","Spades", "Diamonds", "Clubs"]
        values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Aces":14}#14 = As 13=King 12=Queen 11=Jacks
    
        for name in values:
            for suit in suits:
                self.cards.append( Card(name,values[name],suit))

    def __repr__(self):
        return "Standard Deck of cards {0} cards remaining".format(len(self.cards))#mostra o tanto de cartas que estão faltando no deck

class Player(object):
    def __init__(self,cards):
        self.cards = []
    def numberOfCards(self):
        return len(self.cards)
        
class PokerScorer(object):
    def __init__(self):
    #number of cards 
        if not len(cards) == 5:
            return "Error : Wrong number of cards."
        self.cards = cards

    def suitCount(self):
        suits = [card.suit in self.cards]
        return list(set(suit))
    def straight(self):
        values = [cards.value for card in self.cards]
        values.sort()
        if not len(set(values)) ==5:
            return False
        
        if value[5] == 14:
            pass
        else:
            if not value[0]+1 == value[1]: return False
            if not value[1]+1 == value[2]: return False
            if not value[2]+1 == value[3]: return False
            if not value[3]+1 == value[4]: return False
        return True
        #consecutive numbers
        #values = [for card in self.cards]
        
        tests = [[14,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],[8,13],[9,14]]
        for test in tests:
            if test[0] in values and test[1] in values:
                return False
        #comprova se fez uma sequencia para fazer flush    
        #[2,3,4,5,6]
        
    
    
    
    
    