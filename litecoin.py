# THE BIT LIBRARY IS NEEDED https://github.com/ofek/bit
#from coinkit import BitcoinPublicKey
#from pybitcoin import BlockcypherClient
from bit import PrivateKeyTestnet
from bit.network import get_fee, get_fee_cached, NetworkAPI, satoshi_to_currency
import ASUS.GPIO as GPIO
import time
import os

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

	def print_connection_info(self):
		a = PrivateKeyTestnet(self.key_val)
		x = a.get_transactions()
		## print(test.address)
		self.balance = a.get_balance('usd')
		print("Balance: $", self.balance)
		print("Address: ", a.address)
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
		
	def hit(self, card_value):
		
		score = score + card_value
		if (score == 21)
			gameOver = True
		elif (score > 21)
			gameOver = True
		else
			pass
			
	def gameover(self):
		
		if (score == dealer_hand):
			win_lose = 3  # blackjack
			calculate_winning()
		elif (win_lose == 4):  # even
			calculate_winning()
		elif (score > dealer_hand and score <= 21):
			win_lose = 1  # win
			calculate_winning()
		else:
			win_lose = 2  # lose
			calculate_winning()

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


    #while True:
        # Initializing players
	player_1 = Player()
	player_2 = Player()
	player_3 = Player()

	player_1.deposit()
	player_1.print_connection_info()
	    #player_1.withdraw()
	    # Button Press stubs

	    # Deposits
	player_1_deposit = 0
	player_2_deposit = 0
	player_3_deposit = 0

	    # Deal
	player_1_deal = 0
	player_2_deal = 0
	player_3_deal = 0

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
