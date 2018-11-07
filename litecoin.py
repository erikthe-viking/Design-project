#from bit import key
from bit import PrivateKeyTestnet
from bit.network import get_fee, get_fee_cached, NetworkAPI, satoshi_to_currency

# Test Net https://live.blockcypher.com/btc-testnet/
class Player:

    return_address = 'mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2'
    key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
    bet_ammount = 0
    winnings = 1
    win_lose = False
    gameOver = False
    balance = 0

    def print_connection_info(self):
        a = PrivateKeyTestnet(self.key_val)
        x = a.get_transactions()
        self.balance = a.balance
        print("Balance: ", a.balance)
        print("Address: ", a.address)
        print("Return Address: ",self.return_address)
        print("Key Value: ", self.key_val)
        print("Previous Transactions: ", x)
      #  z = PrivateKeyTestnet.prepare_transaction('mfhndBrGKSXuLgd8RbWcxkhQGSBqwQXVF2', [('92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3', 1, 'jpy')])
       # print(z)

    def deposit(self):
        key_class = PrivateKeyTestnet(self.key_val)
        tran = key_class.get_transactions()
        if len(tran) > 0:
            if tran[0] != self.return_address:
                self.return_address = tran[0]
               # print (self.address)
            else:
                print ("weiner")
            

    def withdraw(self):
        rv = conn.validateaddress(self.address)
        key = PrivateKeyTestnet(self.key_val)

        if self.winnings <= self.balance:
            print ("The withdrawl address is valid")
            key.create_transaction([(self.return_address, self.winnings, 'jpy')])
        else:
            print ("Not in enough coins in balance")
    def calculate_winning(self):
        self.winnings = bet_amount * 1.5
        
    def stay(self):
        pass
    def deal(self):
        pass
  

def main():
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

