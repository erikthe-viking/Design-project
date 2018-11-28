# THE BIT LIBRARY IS NEEDED https://github.com/ofek/bit


#from coinkit import BitcoinPublicKey
#from pybitcoin import BlockcypherClient
from bit import PrivateKeyTestnet
from bit.network import get_fee, get_fee_cached, NetworkAPI, satoshi_to_currency
import ASUS.GPIO as GPIO
import time
import os
import blockcypher
import random
#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import resources # Image Recognition Library
# https://tinkerboarding.co.uk/wiki/index.php/GPIO#Python GPIO
import MotorController 
wallet = PrivateKeyTestnet('93ABUFDeHRB1M9aLcHp5PrHdHyLsRTcz1pyHNx3HHiGKvLWWAAC')
#print(wallet.get_balance)
#wallet.create_transaction([("myrqQVsq4MCmjBeCpFt8v8HfUPeHrysftg",15, 'usd')],combine=False)
#print(wallet.address)
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
                                    if ((score + 11) > 21):
                                                score = score + 1
                                    else:
                                                score = score + 11
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

    return_address = 'myrqQVsq4MCmjBeCpFt8v8HfUPeHrysftg'
    old_key_val = '92DTyQmsrsy4yWUvHpdyjPsF7WxDd6E13g43DXnyTthF3UrgfS3'
    key_val = '93ABUFDeHRB1M9aLcHp5PrHdHyLsRTcz1pyHNx3HHiGKvLWWAAC'
    bet_ammount = 0
    winnings = 1
    win_lose = False
    gameOver = False
    balance = 10    
    score = 0
    #wallet = PrivateKeyTestnet(key_val)
    tinkerboard_address = "mgrLnEH453rCP8fGtKDLarPH6E6uHegtkD"
    win_lose = False    
    transaction_size = 0

    def print_connection_info(self):
    
        x = wallet.get_transactions()

        self.transaction_size = len(x)
#        print(len(x))
        self.balance = wallet.get_balance("usd")
        print("Balance: $", self.balance)
        print("Address: ", wallet.address)
        print("Return Address: ",self.return_address)
        print("Key Value: ", self.key_val)
        print("Previous Transactions: ", x[0])
        

    def deposit(self): 
        x = wallet.get_transactions()
        
        if len(x) > self.transaction_size:
            print("Deposit Recieved")        
            self.transaction_size = len(x)        
  #          test = blockcypher.get_transaction_details(x[0],coin_symbol="btc-testnet",api_key="b0c2292b9bc84058adba7f8bd4bf2698")
   #         a = test['outputs']
    #        print(a[0]['value'])
     #       self.bet_ammount = a[0]['value']
            return True
        else:
            print("Not received Deposit")
            return False


    def test_w(self):
            wallet.send([("myrqQVsq4MCmjBeCpFt8v8HfUPeHrysftg",20, 'usd')],combine=False)
            

    def withdraw(self):
    
        win = float(2)
        bal = float(self.balance)
        
        if win <= bal:
            print ("The withdrawl address is valid")
            print(wallet.create_transaction([(self.return_address,win, 'usd')],combine=False))
        else:
            print ("Not in enough coins in balance")

   
def main():

    # Button GPIO pins
    Player_1_hit = 37
    Player_1_stay = 38
    Player_1_withdraw = 40

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Player_1_hit,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Player 1 blue
    GPIO.setup(Player_1_stay,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Player 1 yellow
    GPIO.setup(Player_1_withdraw,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Player 1 white

    player_1 = Player()
    player_1.print_connection_info()
   # player_1.withdraw()
    deposit = False
    card_state = "" # Card State
    house_sum = 0
    test = True
    # Needs to have internal random card dealt to house state
    # Game Loop
    controller = MotorController.MotorController()
    controller.PrimeTrack() # primes card dealing mechanism
    cards = 'A23456789TQJK'
    counter = 0
    while True:
        counter = counter + 1
        dealer_hand = random.choice(cards)
        dealer_hand+='?'
        if card_state == "" and deposit == False: # Checks to see if it is a new game
            deposit = player_1.deposit()
        
        if player_1.score > 21:
            print ("Bust")
            break

        if deposit == True: # If a Deposit is recieved
            if  counter == 1:
               card_state = resources.recognize_cards() # Calls Image Recognition
            print("card State: ", card_state)            
            # Loop that sums the cards
            player_1.score = calculateHand(card_state) # Calculates hand total
            print (player_1.score)
            
            if GPIO.input(Player_1_hit) == GPIO.HIGH: # Calls Deal functions
                print ("Card Dealt")
               # Deal Card
                controller.DealCard()
                time.sleep(5)
                card_state = resources.recognize_cards()
            if GPIO.input(Player_1_stay) == GPIO.HIGH:
                print("Player Stay:")
                time.sleep(2)
                card_state = resources.recognize_cards()
                dealer_hand = dealer_hand[:-1]
                dealer_hand+=random.choice(cards)
                while True:
                    house_sum = calculateHand(dealer_hand) # calculate dealer score
                    if (house_sum <= 17):
                        dealer_hand+=random.choice(cards)
                    else:
                        break
                if player_1.score <= 21:
                    if house_sum > 21:
                        print("House Sum:", house_sum)
                        player_1.withdraw()
                        print("You Won the Game! Money Withdrawn")
                        break
                    elif (player_1.score > house_sum) and house_sum < 21:
                        print("House Sum:", house_sum)
                        player_1.withdraw()
                        print("You Won the Game money Withdrawn")
                         # Call withdraw function
                        break
                    elif player_1.score == house_sum and house_sum <= 21:
                        print("House Sum", house_sum)
                        print("Tie")
                    else:
                        print("House Sum:", house_sum)
                        print("You Lost Punk!")
                        break
                else:
                    print("House Sum:", house_sum)
                    print("You Lost Punk!")
                    break
        
                
if __name__ == "__main__":
    main()


