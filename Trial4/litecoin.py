# THE BIT LIBRARY IS NEEDED https://github.com/ofek/bit
#from coinkit import BitcoinPublicKey
#from pybitcoin import BlockcypherClient
from bit import PrivateKeyTestnet
from bit.network import get_fee, get_fee_cached, NetworkAPI, satoshi_to_currency
import ASUS.GPIO as GPIO
import time
import os
import blockcypher
#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import resources # Image Recognition Library
# https://tinkerboarding.co.uk/wiki/index.php/GPIO#Python GPIO
import MotorController

def calculateHand(string):
	score = 0
	for i in range(0,len(string)):
                                if string[i] == "K":
                                        score = score + 10
                                if string[i] == "J":
                                        score = score + 10
                                if string[i] == "Q":
                                        score = score + 10
                                if string[i] == "A":
                                        if score + 11 > 21:
                                                score = score + 1
                                        else:
                                                score = score + 11
                                if string[i] == "1":
                                        score = score + 1
                                if string[i] == "2":
                                        score = score + 2
                                if string[i] == "3":
                                        score = score + 3
                                if string[i] == "4":
                                        score = score + 4
                                if string[i] == "5":
                                        score = score + 5
                                if string[i] == "6":
                                        score = score + 6
                                if string[i] == "7":
                                        score = score + 7
                                if string[i] == "8":
                                        score = score + 8
                                if string[i] == "9":
                                        score = score + 9
                                if string[i] == "T":
                                        score = score + 10
	return score
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
			return True
		else:
			print("Not received Deposit")
			return False


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
#	test = resources.recognize_cards()
#	print(test)
#	blockcypher.get_token_info("b0c2292b9bc84058adba7f8bd4bf2698")
	# Button GPIO pins
	Player_1_hit = 37
	Player_1_stay = 38
	Player_1_withdraw = 40

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Player_1_hit,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Player 1 blue
	GPIO.setup(Player_1_stay,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Player 1 yellow
	GPIO.setup(Player_1_withdraw,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Player 1 white
	GPIO.setup(11,GPIO.IN)# Player 2 blue
	GPIO.setup(13,GPIO.IN)# Player 2 yellow
	GPIO.setup(15,GPIO.IN)# Player 2 white
	GPIO.setup(19,GPIO.IN)# Player 3 blue
	GPIO.setup(21,GPIO.IN)# Player 3 yellow
	GPIO.setup(23,GPIO.IN)# Player 3 white
	# blue = hit, yellow = stay, white = withdraw

#	while True:
		#print("Button values:",GPIO.input(Player_1_hit), GPIO.input(Player_1_stay), GPIO.input(Player_1_withdraw))
#		if GPIO.input(Player_1_hit) == GPIO.HIGH:
#			print ("hello")
#		if GPIO.input(Player_1_stay) == GPIO.HIGH:
#			print ("stay")
#		if GPIO.input(Player_1_withdraw) == GPIO.HIGH:
#			print ("withdraw")



	player_1 = Player()
	player_1.print_connection_info()
	
	deposit = False
	card_state = "" # Card State
	house_sum = 0


	# Game Loop
	while True:
		if card_state == "" and deposit == False: # Checks to see if it is a new game
			deposit = player_1.deposit()
		
		if player_1.score > 21:
			print ("Bust")
			break

		if deposit == True: # If a Deposit is recieved
			card_state = resources.recognize_cards() # Calls Image Recognition
			
			# Loop that sums the cards
			player_1.score = calculateHand(card_state) # Calculates hand total
			print (player_1.score)

			if GPIO.input(Player_1_hit) == GPIO.HIGH: # Calls Deal functions
				print ("Card Dealt")
				# Deal Card

			if GPIO.input(Player_1_stay) == GPIO.HIGH:
				if player_1.score > house_sum and player_1.score <= 21:
					player_1.withdraw()
					 # Call withdraw function
		
				
if __name__ == "__main__":
    main()


