# coding: utf-8
from cards import Cards, Deck, Player, Dealer

blackjack = """\033[1;33m
	__________.__                 __          ____.              __
	\______   \  | _____    ____ |  | __     |    |____    ____ |  | __
	 |    |  _/  | \__  \ _/ ___\|  |/ /     |    \__  \ _/ ___\|  |/ /
	 |    |   \  |__/ __ \   \___|    <  /\__|    |/ __ \   \___|    <
	 |______  /____(____  /\___  >__|_ \ \________(____  /\___  >__|_ \
	        \/          \/     \/     \/               \/     \/     \/
\033[1;m
"""

symbols= """\033[1;31m
			                               _
			       ,'`.    _  _    /\    _(_)_
			      (_,._)  ( `' )  <  >  (_)+(_)
			        /\     `.,'    \/      |
\033[1;m
"""
print blackjack
print symbols

name = raw_input("What is your name? ") # Asks user what their name is
# chip = input("How many starter chips do you want? ") # ask user how many starter chips they want
# while type(chip)!= int:  # if whatever they typed in is not an integer, it makes the user type again
# 	chip = input("Please put an integer. Dummy. ")
# bet = input("How much do you want to wager each time? (Please type an integer) ")
# while type(bet) != int:
# 	bet = input("Please put an integer. Dummy. ")

myDeck = Deck() # create Deck object
player = Player(name) # create Player object
dealer = Dealer() # create Dealer object

def start_game(): # start game function
	myDeck.create() # creates the deck
	myDeck.shuffle() # shuffles the deck
	myDeck.deal(player, dealer) # deals the cards to the players and prints message

def the_game(): # function that plays the game
	myDeck.reset(player, dealer) # every time the game starts/restarts, the cards are reset
	start_game() # calls the start_game function and starts the game
	print "Your total value is \033[1;33m{}\033[1;m".format(player.sum) # prints out total value

	if dealer.sum == 21 and player.sum == 21: # if both dealer and player gets a black jack initially
		print "Double black jack! You tied!"
		return # exits the game
	elif dealer.sum == 21: # if the dealer gets a black jack
		print "Dealer got black jack! Game ends. You a loser"
		lose() # calls the lose function because you lost
		return
	elif player.sum == 21: # if the player gets a black jack
		print "You got a black jack! Game ends."
		win() # calls the win function
		return

	answer2 = raw_input("\nDo you want to hit or stay? (H = hit; S = stay)") # asks player if they want to hit or stay
	while answer2.upper()!='H' and answer2.upper()!='S':
		answer2 = raw_input("Please type H for Hit and S for Stay: ")
	while answer2.upper() == 'H': # while the answer2 is "H" aka hit
		player.hit(myDeck) # player hits
		print "Your total value is \033[1;33m{}\033[1;m".format(player.sum)

		hand_sum = player.sum # equals the the total value of player
		if hand_sum>21: # if the total is greater than 21
			print "You're a Loser!"
			lose() # you lose
			return
		else: # else
			answer2 = raw_input("\nDo you want to hit or stay? (H = hit; S = stay)") # prompts H/S question again
			while answer2.upper()!='H' and answer2.upper()!='S':
				answer2 = raw_input("Please type H for Hit and S for Stay: ")
			# if user answers H, while loop will continue
			# if user answer S, then exits the while loop and goes to next code
	if answer2.upper() == 'S': # when the user answers S
		player.stay()
		while(dealer.sum < 17): #
			dealer.hit(myDeck)
		if dealer.sum > 21:
			print "Dealer bust at \033[1;31m{}\033[1;m! Player wins!".format(dealer.sum)
			win()
			return
		elif dealer.sum > player.sum:
			print "Dealer wins \033[1;31m{}-{}\033[1;m. You lost. Loser".format(dealer.sum, player.sum)
			lose()
			return
		elif dealer.sum < player.sum:
			print "You win \033[1;31m{}-{}\033[1;m. You're not a loser. I guess".format(player.sum, dealer.sum)
			win()
			return
		else:
			print "You tied \033[1;31m{}-{}\033[1;m. That's weird".format(player.sum, dealer.sum)
			return
def make_bet():
	bet = None
	while True:
		try:
			bet = int(input("\nHow many chips do you want to bet? (Please type an integer)"))
		except:
			print('\n Enter an integer. Dummy')
		else:
			break
	return bet

answer = raw_input("\nAre you ready to start the game? (Y/N)")
while answer.upper()!='Y' and answer.upper()!='N':
	answer = raw_input("Please enter Y or N: ")
while(answer.upper() == 'Y'):
	print '\nYou have \033[1;35m{}\033[1;m chips'.format(player.chips)
	# bet = input("\nHow many chips do you want to bet? (Please type an integer) ")
	bet = make_bet()
	def lose(): # function for when you lose
		player.chips-=bet # you lose however much you bet
		print """
	 __   _____  _   _   _     ___  ____  _____     _______           _______
	 \ \ / / _ \| | | | | |   / _ \/ ___|| ____|   / /_   _|         |_   _\ \
	  \ V / | | | | | | | |  | | | \___ \|  _|    | |  | |             | |  | |
	   | || |_| | |_| | | |__| |_| |___) | |___   | |  | |             | |  | |
	   |_| \___/ \___/  |_____\___/|____/|_____|  | |  |_|    _____    |_|  | |
	                                               \_\       |_____|       /_/
			"""
		print "You lost \033[1;31m{}\033[1;m chips. You currently have \033[1;31m{}\033[1;m\n".format(bet, player.chips)
		if player.chips<=0: # if loser run out of chips
			print """
	                              )
	 (                         ( /(
	 )\ )      )    )     (    )\())  )     (  (
	(()/(   ( /(   (     ))\  ((_)\  /((   ))\ )(
	 /(_))_ )(_))  )\  '/((_)   ((_)(_))\ /((_|()\
	(_)) __((_)_ _((_))(_))    / _ \_)((_|_))  ((_)
	  | (_ / _` | '  \() -_)  | (_) \ V // -_)| '_|
	   \___\__,_|_|_|_|\___|   \___/ \_/ \___||_|

				"""
			print "\033[1;41mYou have no more chips. Get out!\033[1;m"
			exit() # exit out of the game because player is a loser
	def win(): # function for when player wins
		player.chips+=bet # adds however much you bet to the total about of chip
		print """

	Y)    yy  O)oooo  U)    uu    W)      ww I)iiii N)n   nn
	 Y)  yy  O)    oo U)    uu    W)      ww   I)   N)nn  nn
	  Y)yy   O)    oo U)    uu    W)  ww  ww   I)   N) nn nn
	   Y)    O)    oo U)    uu    W)  ww  ww   I)   N)  nnnn
	   Y)    O)    oo U)    uu    W)  ww  ww   I)   N)   nnn
	   Y)     O)oooo   U)uuuu      W)ww www  I)iiii N)    nn


				"""
		print "You gained \033[1;32m{}\033[1;m chips. You currently have \033[1;32m{}\033[1;m\n".format(bet, player.chips)

	the_game()
	answer = raw_input("Do you want to play again? (Y/N)")
	while answer.upper()!='Y' and answer.upper()!='N':
		answer = raw_input("Please enter Y or N: ")
