#-----------------------------------------
# This code is a modified version of the
# playing card detector code by Evan Juras
# Also utilizes the Cards library by 
# Evan Juras
#-----------------------------------------

import sys, os, cv2
import numpy as np
import Cards

#print(cv2.__version__)

def name_format(word):
		return{
			'Ace': 'A',
			'Two': '2',
			'Three': '3',
			'Four': '4',
			'Five': '5',
			'Six': '6',
			'Seven': '7',
			'Eight': '8',
			'Nine': '9',
			'Ten': 'T',
			'Jack': 'J',
			'Queen': 'Q',
			'King': 'K',
			'Unknown': 'U',
			}[word]

def recognize_cards():
	
	result = ""
	# Initinalizes the camera for capture
	cap = cv2.VideoCapture("v4l2src ! video/x-raw, format = NV12, width=1280, height=960 ! videoconvert! appsink")
	#cap = cv2.VideoCapture(0)
	font = cv2.FONT_HERSHEY_SIMPLEX
	
	# Specifies training card location
	path = os.path.dirname(os.path.abspath(__file__))
	train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
	train_suits = Cards.load_suits( path + '/Card_Imgs/')
	
	# Takes a snapshot
	ret, frame = cap.read()
	#frame = cv2.imread("test_img/card7.jpg",1)
	#cv2.imshow("test_img",frame)
	#cv2.waitKey(0)
    	#cap.release()
	# Processes and sorts cards, check which contours are actually cards
	processed_cards = Cards.preprocess_image(frame)
	sorted_contours, card_contour = Cards.find_cards(processed_cards)
	#cv2.drawContours(frame, sorted_contours, -1, (255,0,0), 2)
	if len(sorted_contours) != 0:
		cards = []
		k = 0
	
		for i in range(len(sorted_contours)):
			if(card_contour[i] == 1):
	
				cards.append(Cards.preprocess_card(sorted_contours[i], frame))
	
				cards[k].best_rank_match, cards[k]. best_suit_match, cards[k]. rank_diff, cards[k].suit_diff = Cards.match_card(cards[k], train_ranks, train_suits)
	
				result += name_format(cards[k].best_rank_match)
				
				frame  = Cards.draw_results(frame, cards[k])
				k = k+1
		if(len(cards) != 0):
			temp_cnts = []
			for i in range(len(cards)):
				temp_cnts.append(cards[i].contour)
			cv2.drawContours(frame, temp_cnts, -1, (255,0,0), 2)
	cv2.imshow("Card Detector", frame)
	cv2.waitKey(0)
		
	# Clean up
	#cap.release()
	#cv2.waitKey(0)
	cv2.destroyAllWindows()
	return result
