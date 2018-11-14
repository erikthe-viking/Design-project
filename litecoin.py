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
	
		if (win_lose == 4):  # blackjack
			self.winnings = bet_amount + (bet_amount * 1.5)
		elif (win_lose == 3):  # even
			self.winnings = bet_amount
		elif (win_lose == 1):  # win
			self.winnings = bet_amount * 2
		else:  # lose
			self.winnings = 0

	def stay(self):
		pass
		
	def hit(self, hand):
		
		# hand is a string that returns all players' cards (ex. "Player 1: A 10 \n Player 2: 4 J 6 \n Player 3: 10 K")
		# need to parse string and turn each player's cards into a list
		self.hand_values = list(hand)  # temp
		score = sum(self.hand_values)
		if (score == 21):
			gameOver = True
		elif (score > 21):
			gameOver = True
		else:
			print("player x score: {0}".format(score))
	
	def initial_deal(self, hand, player_num):
		
		# hand is a string that returns all players' first two cards (ex. "Player 1: A 10 \nPlayer 2: 4 J \nPlayer 3: 10 K ")
		# need to parse string and turn each player's cards into a list
		if (player_num == 1):
			hand, sep, tail = hand.partition('Player 2: ')
			head, sep, hand = hand.partition(': ')
		elif (player_num == 2):
		elif (player_num == 3):
		self.hand_values = list(hand)  # temp
		score = sum(self.hand_values)
		if (score == 21):
			gameOver = True
		else:
			print("player x score: {1}".format(score))
		
		
	def gameover(self):
		
		if (score == Dealer.score):
			win_lose = 3  # blackjack
			calculate_winning()
			balance = balance + self.winnings
		elif (win_lose == 4):  # even
			calculate_winning()
			balance = balance + self.winnings
		elif (score > Dealer.score and score <= 21):
			win_lose = 1  # win
			calculate_winning()
			balance = balance + self.winnings
		else:
			win_lose = 2  # lose
			calculate_winning()
			balance = balance + self.winnings

class Dealer:

	return_address = 'mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2'
	key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
	gameOver = False
	score = 0
	
	def hit(self, hand):
		
		score = list(hand)
		if (score <= 17):
			hit()

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

	img_rec = "Player 1: A Q\nPlayer2: J 5\nPlayer 3: 7 2"

    #while True:
        # Initializing players
	player_1 = Player()
	player_2 = Player()
	player_3 = Player()
	dealer = Dealer()

	players = [player_1, player_2, player_3]
	pool = cycle(lst)

	for item in pool:
		if (item == pool[0]):
			player_num = 1
		elif (item == pool[1]):
			player_num = 2
		else:
			player_num = 3
		item.initial_deal(img_rec, player_num)
		

	player_1.deposit()
	player_1.print_connection_info()
	    #player_1.withdraw()
	    # Button Press stubs

	    # Deposits
	player_1_deposit = 0
	player_2_deposit = 0
	player_3_deposit = 0

	    # Stay
	player_1_stay = 0
	player_2_stay = 0
	player_3_stay = 0
	
	if Player_1_hit != 0:
		player_1.hit()
	if Player_2_hit != 0:
		player_2.hit()
	if Player_3_hit != 0:
		player_3.hit()
	
	if Player_1_stay != 0:
		player_1.stay()
	if Player_2_stay != 0:
		player_2.stay() 
	if Player_3_stay != 0:
		player_3.stay() 

	if Player_1_withdraw != 0:
		player_1.withdraw() 
	if Player_2_withdraw != 0:
		player_2.withdraw() 
	if Player_3_withdraw != 0:
		player_3.withdraw() 
					
if __name__ == "__main__":
    main()
