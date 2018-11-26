#-----------------------------------------
# This code is a modified version of the
# playing card detector code by Evan Juras
# Also utilizes the Cards library by 
# Evan Juras
#-----------------------------------------

import sys, os, cv2
import numpy as np
import Cards

print(cv2.__version__)
cv2.setNumThreads(4)
# Initinalizes the camera for capture
cap = cv2.VideoCapture("v4l2src ! video/x-raw, format = NV12, width=1280, height=960 ! videoconvert! appsink")
#cap = cv2.VideoCapture("1 ! video/x-raw, formate = NV12, width=1280, height=960 ! videoconvert! appsink")
#cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,512)
font = cv2.FONT_HERSHEY_SIMPLEX

path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
train_suits = Cards.load_suits( path + '/Card_Imgs/')

# Run while camera is running
while cap.isOpened():
	# Retreives each frame of the video capture
	ret, frame = cap.read()
	
	#----------------------------------------------------------------------------------------
	# Transforms the image and finds the contour
	#kernel = np.ones((5,5),np.uint8)
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#blur = cv2.GaussianBlur(gray,(1,1),1000)
	#edge = cv2.Canny(blur, 175, 200)	

	#flag, thresh = cv2.threshold(edge, 120, 255, cv2.THRESH_BINARY)
	#im, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	# Sorts the contour from largest to smallest	
	#sorted(contours, key=cv2.contourArea, reverse=True)
	
	#----------------------------------------------------------------------------------------
	processed_cards = Cards.preprocess_image(frame)

	sorted_contours, card_contour = Cards.find_cards(processed_cards)
	#cv2.drawContours(frame, sorted_contours, -1, (0,255,0),3)

	if len(sorted_contours) != 0:
		cards = []
		k = 0

		for i in range(len(sorted_contours)):
			if(card_contour[i] == 1):

				cards.append(Cards.preprocess_card(sorted_contours[i], frame))

				cards[k].best_rank_match, cards[k]. best_suit_match, cards[k]. rank_diff, cards[k].suit_diff = Cards.match_card(cards[k], train_ranks, train_suits)

				frame  = Cards.draw_results(frame, cards[k])
				k = k+1

		if(len(cards) != 0):
			temp_cnts = []
			for i in range(len(cards)):
				temp_cnts.append(cards[i].contour)
			cv2.drawContours(frame, temp_cnts, -1, (255,0,0), 2)

	cv2.imshow("Card Detector", frame)

	
	# For each of the contours
	#for i,c in enumerate(contours):
		
		# Extract the location and size of the countour
		#[x,y,w,h] = cv2.boundingRect(c)
		
		# Filter contours that are too small or too large
		#if h*w > 50000:
		#	continue
		#if h<150 or w<150:
		#	continue
		
		# Flattens the image of the card
		#peri = cv2.arcLength(c, True)
		#approx = cv2.approxPolyDP(c, 0.01*peri, True)
		#pts = np.float32(approx)
		
		#wrap = resources.flattener(frame, pts, w, h)
	
		# Displays the cropped and flattened card image
		#cropped = frame[y: y+h, x: x+w]
		#cv2.imshow("Flattened", wrap)
		#cv2.imshow("Cropped", cropped)
		#box = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
	
	#cv2.drawContours(frame, contours, -1, (255,0,0),3)
	#cv2.imshow("temp", frame)		
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
	
# Clean up
cap.release()
cv2.destroyAllWindows()
