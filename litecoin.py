# THE BIT LIBRARY IS NEEDED https://github.com/ofek/bit
#from coinkit import BitcoinPublicKey
#from pybitcoin import BlockcypherClient
from bit import PrivateKeyTestnet
from bit.network import get_fee, get_fee_cached, NetworkAPI, satoshi_to_currency
import ASUS.GPIO as GPIO
import time
import os
from itertools import cycle

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# https://tinkerboarding.co.uk/wiki/index.php/GPIO#Python GPIO

# Test Net https://live.blockcypher.com/btc-testnet/
class Player:

	return_address = 'mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2'
	key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
	bet_amount = 0
	winnings = 1
	# 0 = still playing, 1 = win, 2 = lose, 3 = even, 4 = blackjack
	win_lose = 0
	gameOver = False
	balance = 10	
	score = 0
	hand_values = [None] * 10
	a = PrivateKeyTestnet(self.key_val)
	
	def reset(self):
		
		return_address = 'mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2'
		key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
		bet_amount = 0
		winnings = 1
		# 0 = still playing, 1 = win, 2 = lose, 3 = even, 4 = blackjack
		win_lose = 0
		gameOver = False
		balance = 10	
		score = 0
		hand_values = [None] * 10
		a = PrivateKeyTestnet(self.key_val)

	def print_connection_info(self):
		
		x = a.get_transactions()
		## print(test.address)
		self.balance = a.get_balance('usd')
		print("Balance: $", self.balance)
		print("Address: ", self.a.address)
		print("Return Address: ",self.return_address)
		print("Key Value: ", self.key_val)
		print("Previous Transactions: ", x)
 

	def deposit(self):
		key_class = PrivateKeyTestnet(self.key_val)
		tran = key_class.get_transactions()
		if len(tran) > 0:
			if tran[0] != self.return_address:
				self.return_address = tran[0]
               # prin://www.maac.com/texas/dallas/post-addison-circlet (self.address)
		else:
			print ("weiner")
            

	def withdraw(self):
 
		key = PrivateKeyTestnet(self.key_val)

		if self.winnings <= self.balance:
			print ("The withdrawal address is valid")
			key.create_transaction([(self.return_address, self.winnings, 'usd')])
		else:
			print ("Not in enough coins in balance")

	def calculate_winning(self):
	
		if (self.win_lose == 4):  # blackjack
			self.winnings = self.bet_amount + (self.bet_amount * 1.5)
		elif (self.win_lose == 3):  # even
			self.winnings = self.bet_amount
		elif (self.win_lose == 1):  # win
			self.winnings = self.bet_amount * 2
		else:  # lose
			self.winnings = 0

	def stay(self):
		self.gameOver = True
		
	def hit(self, hand):
		
		self.get_score(hand, player_num)
		if (self.score == 21):
			self.gameOver = True
			self.win_lose = 4
		elif (self.score > 21):
			self.gameOver = True
			self.win_lose = 2
		else:
			print("player {0} score: {1}".format(player_num, self.score))
	
	# get score of current hand
	def get_score(self, hand):
		
		# hand is a string that returns all players' first two cards (ex. "Player: A7 \n Dealer: QQ \n")
		head, sep, hand = hand.partition('Player: ')
		hand, sep, tail = hand.partition(' \n Dealer')
		self.hand_values = list(hand)
		temp = 0
		for n, x in enumerate(self.hand_values):
			if (x == 'A'):
				self.hand_values[n] = '11'
				temp = temp+1  # keep track of how many aces
			elif (x == 'T' or x == 'J' or x == 'Q' or x == 'K'):
				self.hand_values[n] = '10'
		self.hand_values = list(map(int, self.hand_values))
		self.score = sum(self.hand_values)
		while (self.score > 21):  # change values of aces to 1 if they make score greater than 21 as 11s
			if(temp > 0):
				self.score = self.score-10
				temp = temp-1
				
	# first deal (2 cards each)	    
	def initial_deal(self, hand):
		
		self.get_score(hand)
		if (self.score == 21):
			self.gameOver = True
			self.win_lose = 3  # blackjack
		else:
			print("score: {1}".format(self.score))
		
		
	def gameover(self, blackjack_bool, dealer_score):
		
		if (self.win_lose == 4): # blackjack
			if (blackjack_bool == True):
				self.win_lose = 3  # even
			self.calculate_winning()
			self.balance = self.balance + self.winnings
		elif (self.win_lose == 3):  # even
			self.calculate_winning()
			self.balance = self.balance + self.winnings
		elif (self.score > dealer_score and self.score <= 21):
			self.win_lose = 1  # win
			self.calculate_winning()
			self.balance = self.balance + self.winnings
		else:
			self.win_lose = 2  # lose
			self.calculate_winning()
			self.balance = self.balance + self.winnings

class Dealer:

	return_address = 'mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2'
	key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
	gameOver = False
	score = 0
	blackjack = False
	
	def reset(self):
		return_address = 'mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2'
		key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
		gameOver = False
		score = 0
		blackjack = False
	
	def initial_deal(self, hand):
		
		self.get_score(hand)
		if (self.score == 21):
			self.gameOver = True
			self.blackjack == True  # blackjack
		else:
			print("Dealer score: {1}".format(self.score))
			
	def hit(self, hand):
		
		self.get_score(hand)
		if (self.score == 21):
			self.gameOver = True
		elif (self.score > 21):
			self.gameOver = True
		else:
			print("Dealer score: {1}".format(self.score))
	
	def get_score(self, hand):
		
		# hand is a string that returns all players' first two cards (ex. "Player: A7 \n Dealer: QQ \n")
		head, sep, hand = hand.partition('Dealer: ')
		hand, sep, tail = hand.partition(' \n')
		self.hand_values = list(hand)
		self.aces = 0
		for n, x in enumerate(self.hand_values):
			if (x == 'A'):
				self.hand_values[n] = '11'
				self.aces = self.aces+1  # keep track of how many aces
			elif (x == 'T' or x == 'J' or x == 'Q' or x == 'K'):
				self.hand_values[n] = '10'
		self.hand_values = list(map(int, self.hand_values))
		self.score = sum(self.hand_values)
		while (self.score > 21):  # change values of aces to 1 if they make score greater than 21 as 11s
			if(self.aces > 0):
				self.score = self.score-10
				self.aces = self.aces-1

def main():

	# Button GPIO pins
	GPIO.setup(3,GPIO.IN)# Player 1 blue
	GPIO.setup(5,GPIO.IN)# Player 1 yellow
	GPIO.setup(7,GPIO.IN)# Player 1 white

	# blue = hit, yellow = stay, white = withdraw
	Player_1_hit = GPIO.input(3)
	Player_1_stay = GPIO.input(5)
	Player_1_withdraw = GPIO.input(7)

	# temp string
	img_rec = "Player 1: AQ \nDealer: T"
	
        # Initializing players
	player_1 = Player()
	dealer = Dealer()

	# Scan QR-code
	
	while True:
		player_1.reset()
		dealer.reset()
		# deal cards
		dealer.initial_deal(hand)
		player_1.initial_deal(hand)
			
		# allow hits until stay or bust
		while (player_1_hit == 0 and player_1_stay == 0):
			time.sleep(.001)
		while (player_1.gameOver == False):
			if Player_1_hit != 0:
				# deal
				player_1.hit()
			if Player_1_stay != 0:
				player_1.stay()
			
		# still need Dealer at end of game, then restart game
		Dealer.initial_deal()
		while True:
			if (Dealer.gameOver == True):
				break
			elif (Dealer.score <= 16 or (Dealer.score == 17 and Dealer.aces > 0)):  # hit on 16 or soft 17
				Dealer.hit()
			else:
				Dealer.gameOver == True
		
		player_1.gameover()
		
		if Player_1_withdraw != 0:
			player_1.withdraw()
			break
	
	player_1.deposit()
	player_1.print_connection_info()
	    #player_1.withdraw()
	    # Button Press stubs

	    # Deposits
	player_1_deposit = 0
			
if __name__ == "__main__":
    main()
