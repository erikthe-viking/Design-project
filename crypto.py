import jsonrpc 

#access = ServiceProxy("http://user:password@127.0.0.1:8332")
#access.getinfo()
#access.listreceivedbyaddress(6)

#conn = dogecoinrpc.connect_to_local() # Connects to local dogecoin wallet instance


# Print Balance
#print "Your balance is %f" % (conn.getbalance(),)

class Player:
	address = ""
	bet_ammount = 0
	winnings = 0
	win_lose = False
	gameOver = False

	def deposit(self):
		rv = conn.validateaddress(foo)
		if rv.isvalid:
  		  print "The address that you provided is valid"
		else:
  		  print "The address that you provided is invalid, please correct"	
	 
	def withdraw():
		conn.sendtoaddress(address,self.winning) 
	def stay():
		pass
	def deal():
		pass
	def calculate_winning():
		
		self.winnings = bet_amount * 1.5



def main():
	while True:
		# Initializing players
		player_1 = Player()
		player_2 = Player()
		player_3 = Player()

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
