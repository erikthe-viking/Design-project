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
	def get_score(self, hand, player_num):
		
		# hand is a string that returns all players' first two cards (ex. "Player 1: AT \nPlayer 2: 4J \nPlayer 3: TK ")
		if (player_num == 1):
			hand, sep, tail = hand.partition(' \nPlayer 2: ')
			head, sep, hand = hand.partition(': ')
		elif (player_num == 2):
			head, sep, hand = hand.partition('Player 2: ')
			hand, sep, tail = hand.partition(' \nPlayer 3: ')
		elif (player_num == 3):
			head, sep, hand = hand.partition('Player 3: ')
			hand, sep, tail = hand.partition(' \n')
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
	def initial_deal(self, hand, player_num):
		
		self.get_score(hand, player_num)
		if (self.score == 21):
			self.gameOver = True
			self.win_lose = 3  # blackjack
		else:
			print("player {0} score: {1}".format(player_num, self.score))
		
		
	def gameover(self):
		
		if (self.win_lose == 4): # blackjack
			if (Dealer.blackjack == True):
				self.win_lose = 3  # even
			self.calculate_winning()
			self.balance = self.balance + self.winnings
		elif (self.win_lose == 3):  # even
			self.calculate_winning()
			self.balance = self.balance + self.winnings
		elif (self.score > Dealer.score and self.score <= 21):
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
		
		# hand is a string that returns all players' first two cards (ex. "Player 1: AT \nPlayer 2: 4J \nPlayer 3: TK \nDealer: QQ \n")
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
	GPIO.setup(11,GPIO.IN)# Player 2 blue
	GPIO.setup(13,GPIO.IN)# Player 2 yellow
	GPIO.setup(15,GPIO.IN)# Player 2 white
	GPIO.setup(19,GPIO.IN)# Player 3 blue
	GPIO.setup(21,GPIO.IN)# Player 3 yellow
	GPIO.setup(23,GPIO.IN)# Player 3 white

	# blue = hit, yellow = stay, white = withdraw
	Player_1_hit = GPIO.input(3)
	Player_1_stay = GPIO.input(5)
	Player_1_withdraw = GPIO.input(7)
	Player_2_hit = GPIO.input(11)
	Player_2_stay = GPIO.input(13)
	Player_2_withdraw = GPIO.input(15)
	Player_3_hit = GPIO.input(19)
	Player_3_stay = GPIO.input(21)
	Player_3_withdraw = GPIO.input(23)

	# temp string
	img_rec = "Player 1: AQ \nPlayer 2: J5 \nPlayer 3: 72 \nDealer: "
	
        # Initializing players
	player_1 = Player()
	player_2 = Player()
	player_3 = Player()
	dealer = Dealer()

	players = [player_1, player_2, player_3]
	pool = cycle(players)
	
	# Scan QR-code
	
	# Start game once all players are in (even if not 3 players)
	if Player_1_hit != 0 or Player_2_hit != 0 or Player_3_hit != 0:
		# start game
	
	# for indicating which player
	for item in players:
		if (item == players[0]):
			player_num = 1
			# deal cards
			item.initial_deal(img_rec, player_num)
		elif (item == players[1]):
			player_num = 2
			# deal cards
			item.initial_deal(img_rec, player_num)
		else:
			player_num = 3
			# deal cards
			item.initial_deal(img_rec, player_num)
	# deal cards
	Dealer.initial_deal(hand)
			
	# cycling through hits and stays
	# need to wait for input / timing
	for item in pool:
		while True: 
			if (item == pool[0]):
				if Player_1_hit != 0:
					# deal
					item.hit()
				if Player_1_stay != 0:
					item.stay()
				if (item.gameOver == True and pool[1].gameOver == True and pool[2].gameOver == True):
					break
				"""
					if Player_1_withdraw != 0:
						player_1.withdraw()
						break
				"""
			elif (item == pool[1]):
				if Player_2_hit != 0:
					# deal
					item.hit()
				if Player_2_stay != 0:
					item.stay()
				if (item.gameOver == True and pool[0].gameOver == True and pool[2].gameOver == True):
					break
				"""
					if Player_2_withdraw != 0:
						player_2.withdraw()
						break
				"""
			elif (item == pool[2]):
				if Player_3_hit != 0:
					# deal
					item.hit()
				if Player_3_stay != 0:
					item.stay()
				if (item.gameOver == True and pool[0].gameOver == True and pool[1].gameOver == True):
					break
				"""
					if Player_3_withdraw != 0:
						player_3.withdraw()
						break
				"""
			# still need Dealer at end of game, then restart game
	Dealer.initial_deal()
	while True:
		if (Dealer.gameOver == True):
			break
		elif (Dealer.score <= 16 or (Dealer.score == 17 and Dealer.aces > 0)):  # hit on 16 or soft 17
			Dealer.hit()
		else:
			Dealer.gameOver == True
	
	for item in pool:
		item.gameover()
	
	# do withdraw
	
	player_1.deposit()
	player_1.print_connection_info()
	    #player_1.withdraw()
	    # Button Press stubs

	    # Deposits
	player_1_deposit = 0
	player_2_deposit = 0
	player_3_deposit = 0
	
					
if __name__ == "__main__":
    main()
