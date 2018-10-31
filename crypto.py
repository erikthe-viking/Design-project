#from jsonrpc.proxy import JSONRPCProxy
#from jsonrpc import ServiceProxy
import dogecoinrpc

#conn = dogecoinrpc.connect_to_local() # Connects to local dogecoin wallet instance
conn = dogecoinrpc.connect_to_local()
 
class Player:

	address = "D6PTaJLdMj1zfafP9Sep286uGHHusgLNCT"
	bet_ammount = 0
	winnings = 1
	win_lose = False
	gameOver = False

	def print_connection_info(self):
		
		info = conn.getinfo()
		balan = conn.getbalance()
		count = conn.getconnectioncount()
		recieved = conn.listreceivedbyaddress()
		transact = conn.listtransactions()

		print "Balance:", balan
		print "Connection Count:", count
		print "Recieved:", recieved
		print "Transactions:", transact

	def deposit(self):
		pass
		
	def withdraw(self):
		rv = conn.validateaddress(self.address)
		balan = conn.getbalance()
		if rv.isvalid and self.winnings <= balan:
  		  print "The withdrawl address is valid"
		  conn.sendtoaddress(self.address,self.winnings) 
		else:
  		  print "Address or Balance is not valid "
		 
	def stay(self):
		pass
	def deal(self):
		pass
	def calculate_winning(self):
		self.winnings = bet_amount * 1.5
 
def main():

	#while True:
		# Initializing players
		player_1 = Player()
		player_2 = Player()
		player_3 = Player()
		
		player_1.print_connection_info()
		player_1.withdraw()
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

		# Deposit functions
		if player_1_deposit == 1:
			player_1.deposit()
		if player_2_deposit == 1:
			player_2.deposit()
		if player_3_deposit == 1:
			player_3.deposit()

		# Deal
		if player_1_deal == 1:
			player_1.deal()
		if player_2_deal == 1:
			player_2.deal()
		if player_3_deal == 1:
			player_3.deal()

		# Stay
		if player_1_stay == 1:
			player_1.stay()
		if player_2_stay == 1:
			player_2.stay()
		if player_3_stay == 1:
			player_3.stay()

	
		if player_1.gameOver == True:
			player_1.withdraw()
		if player_2.gameOver == True:
			player_2.withdraw()
		if player_3.gameOver == True:
			player_3.withdraw()


if __name__ == "__main__":
    main()

