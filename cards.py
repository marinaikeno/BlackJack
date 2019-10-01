
import random
import copy
suit_symbol = {'Hearts':u"\u2764", 'Diamonds':u"\u25C6", 'Clubs': u"\u2663", 'Spades': u"\u2660"}

class Cards(object): # card class
	def __init__(self, suits, numbers, values):
		self.suits = suits
		self.numbers = numbers
		self.values = values

class Deck(object): # deck class
	def __init__(self):
		self.cards = [] # empty list for deck of cards

	def create(self): # creates all the cards
		suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
		numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
		for suit in suits:
			for number in numbers:
				values = None
				if number == "K" or number == "J" or number  == "Q":
					values = 10
				elif number == 'A':
					values = 11 # default value of Ace is 11
				else:
					values = number
				self.cards.append(Cards(suit, number, values))
	def shuffle(self): # shuffles cards
		for x in range(0,51):
			temp = self.cards[x]
			rand = random.randint(0,51)
			self.cards[x] = self.cards[rand]
			self.cards[rand] = temp

	def reset(self, player, dealer): # reset method that makes all the lists empty
		player.hand = []
		dealer.hand = []
		self.cards = []

	def deal(self, player, dealer): # deals cards to player and dealer
		for i in range(0,4):
			hand = self.cards.pop(0)
			if i<2:
				player.hand.append(hand)
			else:
				dealer.hand.append(hand)
		player.add()
		dealer.add()

		suit_symbol = {'Hearts':u"\u2764", 'Diamonds':u"\u25C6", 'Clubs': u"\u2663", 'Spades': u"\u2660"}

		card_list = []
		for x in player.hand:
			symbol = suit_symbol[x.suits]

			if x.numbers == 10:
				card_number = 10
			else:
				card_number = str(x.numbers)+" "
			card_list.append(card_number)
			card_list.append(symbol)

		print """
 ____________	 ____________
|            |	|            |
| {}         |	| {}         |
|            |	|            |
|            |	|            |
|            |	|            |
|     {}     |	|     {}     |
|            |	|            |
|            |	|            |
|            |	|            |
|         {} |  |         {} |
|____________|	|____________|
			""".format(card_list[0], card_list[2], card_list[1].encode("utf-8")+' ', card_list[3].encode("utf-8")+' ', card_list[0], card_list[2])

		print "\nYou drew \033[1;36m{} of {}\033[1;m and \033[1;36m{} of {}\033[1;m".format(player.hand[0].numbers, player.hand[0].suits, player.hand[1].numbers, player.hand[1].suits)

class Player(object):
	def __init__(self, name):
		self.hand = []
		self.sum = 0
		self.name = name
		self.chips = 100 # default number of chips is 100

	def hit(self, deck):
		hand1 = deck.cards.pop(0) # removes the card from the first index in the deck, and set variable hand1 to that removed card
		self.hand.append(copy.deepcopy(hand1)) # appends a deep copy of the removed card into list 'hand'
		self.add() # add() returns the sum, and passed to variable 'hand_sum'

		# to print out ascii pic of card
		symbol = suit_symbol[hand1.suits]
		card_number=""
		if hand1.numbers == 10:
			card_number = 10
		else:
			card_number = str(hand1.numbers)+" "
		print """
		 ____________
		|            |
		| {}         |
		|            |
		|            |
		|            |
		|     {}     |
		|            |
		|            |
		|            |
		|         {} |
		|____________|

		""".format(card_number,symbol.encode("utf-8")+' ',card_number)
		# print out what player drew
		print "\n{} drew \033[1;36m{} of {}\033[1;m".format(self.name, hand1.numbers, hand1.suits)
		# to check if Ace is 11 or 1
		for card in self.hand: # goes through all the cards in your hand
			if card.numbers == "A" and self.sum>21: # check if the card you have is an Ace, and if you sum is over 21
				card.values = 1
				self.add()
				print "Whoops almost busted! We changed your Ace to 1."

	def stay(self):
		pass

	def add(self):
		self.sum = 0
		for i in self.hand: # not taking into consideration of Ace
			self.sum+=int(i.values)
		return self.sum

class Dealer(Player): # inherits from Player, but hit method is altered
	def __init__(self):
		super(Dealer, self).__init__(name='~Ray the Dealer~') # setting default values
	def hit(self,deck): # similar to hit from Player, but doens't print anything
		hand1 = deck.cards.pop(0) # removes the card from the first index in the deck, and set variable hand1 to that removed card
		self.hand.append(copy.deepcopy(hand1)) # appends a deep copy of the removed card into list 'hand'
		self.add() # add() returns the sum, and passed to variable 'hand_sum'
		print
		# to check if Ace is 11 or 1
		for card in self.hand: # goes through all the cards in your hand
			if card.numbers == "A" and self.sum>21: # check if the card you have is an Ace, and if you sum is over 21
				card.values = 1
				self.add()
