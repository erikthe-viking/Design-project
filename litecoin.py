# THE BIT LIBRARY IS NEEDED https://github.com/ofek/bit
#from coinkit import BitcoinPublicKey
#from pybitcoin import BlockcypherClient
from bit import PrivateKeyTestnet
from bit.network import get_fee, get_fee_cached, NetworkAPI, satoshi_to_currency
import ASUS.GPIO as GPIO
import time
import os
import blockcypher
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# https://tinkerboarding.co.uk/wiki/index.php/GPIO#Python GPIO

# Test Net https://live.blockcypher.com/btc-testnet/
class Player:

	return_address = 'mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2'
	key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
	bet_ammount = 0
	winnings = 1
	win_lose = False
	gameOver = False
	balance = 10	
	score = 0
	wallet = PrivateKeyTestnet(key_val)
	sender_address = "msmoicrcYXmzDQtyv21uKRQrFjdnTDnxbP"
	win_lose = False	
	transaction_size = 0

	def print_connection_info(self):
	
		x = self.wallet.get_transactions()
		self.transaction_size = len(x)
#		print(len(x))
		self.balance = self.wallet.get_balance("usd")
		print("Balance: $", self.balance)
		print("Address: ", self.wallet.address)
		print("Return Address: ",self.return_address)
		print("Key Value: ", self.key_val)
		print("Previous Transactions: ", x)
 

	def deposit(self):
		
				
		x = self.wallet.get_transactions()
		
		if len(x) > self.transaction_size:
			print("Deposit Recieved")		
			self.transaction_size = len(x)		
			test = blockcypher.get_transaction_details(x[0],coin_symbol="btc-testnet",api_key="b0c2292b9bc84058adba7f8bd4bf2698")
			a = test['outputs']
			print(a[0]['value'])
			self.bet_ammount = a[0]['value']



	def test_w(self):
        	a = self.wallet.send([(self.sender_address,3, 'usd')],combine=False)
        	print(a)

	def withdraw(self):
	
		win = float(self.winnings)
		bal = float(self.balance)
		
		if win <= bal:
			print ("The withdrawl address is valid")
			self.wallet.create_transaction([(self.return_address,win, 'usd')],combine=False)
		else:
			print ("Not in enough coins in balance")

	def calculate_winning(self):
		self.winnings = bet_amount * 1.5

	def stay(self):
		pass
	def hit(self):
		pass
  

def main():

#	blockcypher.get_token_info("b0c2292b9bc84058adba7f8bd4bf2698")
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

	player_1.print_connection_info()
	while True:
		player_1.deposit()
#	player_1.test_w()
	player_2 = Player()
	player_3 = Player()

	#layer_1.deposit()
#	player_1.print_connection_info()
#	player_1.withdraw()
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
	#	player_1.withdraw() 
		pass
	if Player_2_withdraw != 0:
	#	player_2.withdraw() 
		pass
	if Player_3_withdraw != 0:
	#	player_3.withdraw() 
		pass
					
if __name__ == "__main__":
    main()


