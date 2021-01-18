
import random

# Init - setting up the basic values of each card, value, 
#suit, name, showing: que tem a intenção de mostrar para o usuário quando solicitado a sua carta
class Card( object ):
  def __init__(self, name, value, suit, symbol):
    self.value = value
    self.suit = suit
    self.name = name
    self.symbol = symbol
    self.showing = False

#def é utilizado para representar o objeto. Serve para mostrar customizar o que retorna - para saber o status de uma ação.

#se a funcao showing for chamada a pessoa vera as cartas na sua mao
#Caso não, ela só receberá a mensagem de "carta" que é como se fosse a carta virada
#retorna os valores da sua carta.
  def __repr__(self):
    if self.showing:
      return self.symbol
    else:
      return "Card"

class Deck(object):
    #shuffle: it randomizes the order of items in a list, we call it a randomizes the elements of a list in place
  def shuffle(self, times=1 ):
    random.shuffle(self.cards)
    #This is a convenience alias to resample(*arrays, replace=False) to do random permutations of the collections.
    print("Deck Shuffled")

  def deal(self):
    return self.cards.pop(0)
    #The pop() method removes the item at the given index from the list and returns the removed item.
    #pop utilizei para pegar a última carta do deck

class StandardDeck(Deck):
    #Esta classe Faz a criação do Deck de Cartas, onde utilizamos 2 dicts para referirmos o primeiro para a sua representação,
    #E o segundo para representar o seu valor, que vai ser útil para podermos avaliar depois quais são as cartas altas e entender
    #toda a lógica do poker
  def __init__(self):
    self.cards = []
    suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
    values = {"Two":2,
              "Three":3,
              "Four":4,
              "Five":5,
              "Six":6,
              "Seven":7,
              "Eight":8,
              "Nine":9,
              "Ten":10,
              "Jack":11,
              "Queen":12,
              "King":13,
              "Ace":14 }
#Para cada nome nos valores, para cada simbolo, será atribuido como string o valor concatenado com seu respectivo símbolo
    for name in values:
      for suit in suits:
        symbolIcon = suits[suit]
        if values[name] < 11:
          symbol = str(values[name])+symbolIcon
        else:
#Como o deck vai até o 10 e depois começa o Jack, então adicionamos o nome e o símbolo.
          symbol = name[0]+symbolIcon
        self.cards.append( Card(name, values[name], suit, symbol) )
  def __repr__(self):
    return "Standard deck of cards:{0} remaining".format(len(self.cards))
#Agora para representar o tanto de cartas que estão restando.

class Player(object):
  def __init__(self):
    self.cards = []
#Uma lista para darmos ao player o seu deck.
  def cardCount(self):
    return len(self.cards)
#Um contador das suas cartas
  def addCard(self, card):
    self.cards.append(card)
#uma função de dar a carta ao jogador

class PokerScorer(object):
  def __init__(self, cards):
    # Number of cards
    if not len(cards) == 5:
      return "Error: Wrong number of cards"
    self.cards = cards
#Mãos de poker: https://www.cardplayer.com/rules-of-poker/hand-rankings
#Flush são 5 cartas do mesmo naipe
  def flush(self):
    suits = [card.suit for card in self.cards]
    if len( set(suits) ) == 1:
      return True
    return False
#5 Valores seguidos, utilizado .sort, e um set para validação
  def straight(self):
    values = [card.value for card in self.cards]
    values.sort()

    if not len( set(values)) == 5:
      return False 
#Como o As pode ser tanto como o numero 1 inteiro tivemos que fazer esta condição.
    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
      return 5

    else:
      if not values[0] + 1 == values[1]: return False 
      if not values[1] + 1 == values[2]: return False
      if not values[2] + 1 == values[3]: return False
      if not values[3] + 1 == values[4]: return False

    return values[4]
#Definição das cartas altas.
#O valor é definiddo por uma comparação dos valores respectivos aquele dicionário.
  def highCard(self):
    values = [card.value for card in self.cards]
    highCard = None
    for card in self.cards:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value: 
        highCard=card

    return highCard

  def highestCount(self):
    count = 0
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) > count:
        count = values.count(value)

    return count
#Definição dos pares, utilizado uma lista para comparar o mesmo valor da carta. 
  def pairs(self):
    pairs = []
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 2 and value not in pairs:
        pairs.append(value)

    return pairs
#Definição para definir se há uma quadrupla, ou seja, comparando o valor se há repetidamente 4 vezes.
  def fourKind(self):
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 4:
        return True

#Uma full house avalia se há 3 cartas iguais e 2 cartas iguais
  def fullHouse(self):
    two = False
    three = False
    
    values = [card.value for card in self.cards]
    if values.count(values) == 2:
      two = True
    elif values.count(values) == 3:
      three = True

    if two and three:
      return True

    return False

#Para se iniciar o Jogo, precisa utilizar no seu emulador o interpreterVideoPoker()
def interpreterVideoPoker():
  player = Player()

  # Intial Amount
  points = 100

  # Cost per hand
  handCost = 10

  end = False
  while not end:
    print( "You have {0} points".format(points) )
    print()

    points-=10

    #utilizado para assim que iniciar o jogo, voce recebe um deck, e ele recebe uma misturada.
    #Hand Loop
    deck = StandardDeck()
    deck.shuffle()

    # Deal Out
    #para entregar ao jogador 5 cartas
    for i in range(5):
      player.addCard(deck.deal())

    #para carta nas mãos deste jogador para este jogador ele verá suas cartas
    # Make them visible
    for card in player.cards:
      card.showing = True
    print(player.cards)

    validInput = False
    while not validInput:
      print("Quais Cartas você quer descartar? ( Ex. 1, 2, 3 )")
      print("Aperte Enter para segurar e escreva exit para sair do jogo ")
      inputStr = input()

      if inputStr == "exit":
        end=True
        break

        #um try para começo da verificação

      try:
        #Transformamos em inteiros, depois dividimos cada número pela virgula.
        inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]
        #validamos caso ele escreva corretamente
        for inp in inputList:
          if inp > 6:
            continue 
          if inp < 1:
            continue 
        #nesta lista, nós entregamos novas cartas e as mostramos para as pessoas
        for inp in inputList:
          player.cards[inp-1] = deck.deal()
          player.cards[inp-1].showing = True

        validInput = True
      except:
        #caso o usuário erre tudo
        print("Input Error: use commas to separated the cards you want to hold")

    print(player.cards)
    #Score
    #Seu cálculo é feito a partir dos pontos que você ganha com cada poder da mão.
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highestCount = score.highestCount()
    pairs = score.pairs()

    # Royal flush
    if straight and flush and straight == 14:
      print("Royal Flush!!!")
      print("+2000")
      points += 2000

    # Straight flush
    elif straight and flush:
      print("Straight Flush!")
      print("+250")
      points += 250

    # 4 of a kind
    elif score.fourKind():
      print("Four of a kind!")
      print("+125")
      points += 125

    # Full House
    elif score.fullHouse():
      print("Full House!")
      print("+40")
      points += 40

    # Flush
    elif flush:
      print("Flush!")
      print("+25")
      points += 25

    # Straight
    elif straight:
      print("Straight!")
      print("+20")
      points += 20

    # 3 of a kind
    elif highestCount == 3:
      print("Three of a Kind!")
      print("+15")
      points += 15

    # 2 pair
    elif len(pairs) == 2:
      print("Two Pairs!")
      print("+10")
      points += 10

    # Jacks or better
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      print("+5")
      points += 5

    player.cards=[]
