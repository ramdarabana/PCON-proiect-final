import numpy as np
import cv2
from pythonosc import osc_server as OSC
from pythonosc.udp_client import SimpleUDPClient

cap = cv2.VideoCapture('https://192.168.1.192:8080/video')

ip = '192.168.1.171'
port = 8000
client = SimpleUDPClient(ip, port) #Create client
print ("OSC Connected")

lower = [200]
lower = np.array(lower, dtype = "uint8")
upper = [255]
upper = np.array(upper, dtype = "uint8")


# set parameters for blob detection
params_W = cv2.SimpleBlobDetector_Params()
params_B = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params_W.minThreshold = 10
params_W.maxThreshold = 1000

params_B.minThreshold = 10
params_B.maxThreshold = 1000


# Filter by Area.
params_W.filterByArea = True
params_W.minArea = 200

params_B.filterByArea = True
params_B.minArea = 300
 

# Filter by Circularity
params_W.filterByCircularity = True
params_W.minCircularity = 0.1

params_B.filterByCircularity = True
params_B.minCircularity = 0.1


# Filter by Convexity
params_W.filterByConvexity = True
params_W.minConvexity = 0.1

params_B.filterByConvexity = True
params_B.minConvexity = 0.1
 
params_W.filterByColor = True
params_W.blobColor = 255

params_B.filterByColor = True
params_B.blobColor = 255

ret, image = cap.read()

left_clicks = list()
white_ons = ""
black_ons = ""
count = 0

# display board
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
ret, image = cap.read()
imS = cv2.resize(image, (900, 800))
cv2.imshow("output", imS)

#### Dimensiune matrice patratica ######
size = 8
###################

whites = np.zeros((size,size))
blacks = np.zeros((size,size))
print (whites)
print (blacks)

# Click pe cele patru colturi ale matricei in ordinea: stanga sus, stanga jos, dreapta jos, dreapta sus
def mouse_callback(event, x, y, flags, params):
	global count
	if(count < 4):
		if(event == 1):
			global left_clicks
			left_clicks.append((x,y))
			print (left_clicks)
			count = count + 1

#set mouse callback function for window
cv2.setMouseCallback("output", mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Determina coordonatele colturilor matricei prin click-stanga
points = list()

(ulx, uly) = left_clicks[0] #stanga sus
(llx, lly) = left_clicks[1] #stanga jos
(lrx, lry) = left_clicks[2] #dreapta jos
(urx, ury) = left_clicks[3] #dreapta sus

# Calculeaza lungimea marginilor
x1 = (ulx + llx) // 2 #margine stanga
x2 = (urx + lrx) // 2 #margine dreapta
y1 = (uly + ury) // 2 #margine sus
y2 = (lly + lry) // 2 #margine jos

print (x1,x2,y1,y2)

# Calculeaza dimensiunea unui patratel (tile) pe x si pe y
tileX = (x2 - x1) // (size - 1)
tileY = (y2 - y1) // (size - 1)

print (left_clicks)

for i in range(size):
	y = y1 + i * tileY
	for j in range(size):
		x = x1 + j * tileX
		points.append((x,y))

cv2.namedWindow('Final', cv2.WINDOW_NORMAL)


while True:
    # Captura stream frame-by-frame
	ret, frame = cap.read()
	frame = cv2.resize(frame, (900, 800))

	# Converteste din color in gray
	gray_W = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray_B = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Invert color pt piese negre
	cv2.bitwise_not(gray_B, gray_B)

	mask_W = cv2.inRange(gray_W, lower, upper)
	detector_W = cv2.SimpleBlobDetector_create(params_W)
	keypoints_W = detector_W.detect(mask_W)

	mask_B = cv2.inRange(gray_B, lower, upper)	
	detector_B = cv2.SimpleBlobDetector_create(params_B)	
	keypoints_B = detector_B.detect(mask_B)

	white_on = ""
	black_on = ""

	for index in range(len(points)):

		row = index // size
		col = index % size

		# Piese albe
		flag_W = False		
		for keyPoint_W in keypoints_W:
			x = keyPoint_W.pt[0]
			y = keyPoint_W.pt[1]
			(xp, yp) = points[index]
			#print (row, col)
			if abs(x - xp) < size and abs(y - yp) < size:
				whites[row][col] = 1
				flag_W = True
				print (row, col, "GOOD")
				white_on += (str(col) + " " + str(row) + " 1 ")
				print ("WHITE")
				print (whites)
		if flag_W == False and whites[row][col] == 1:
			whites[row][col] = 0
			white_on += (str(col) + " " + str(row) + " 0 ")

		# Piese negre
		flag_B = False
		for keyPoint_B in keypoints_B:
			x = keyPoint_B.pt[0]
			y = keyPoint_B.pt[1]
			(xp, yp) = points[index]
			if abs(x - xp) < size and abs(y - yp) < size:
				blacks[row][col] = 1
				flag_B = True
				print (row, col, "GOOD")
				black_on += (str(col) + " " + str(row) + " 1 ")
				print ("BLACK")
				print (blacks)
		if flag_B == False and blacks[row][col] == 1:
			blacks[row][col] = 0
			black_on += (str(col) + " " + str(row) + " 0 ")

	im_with_keypoints_W = cv2.drawKeypoints(mask_W, keypoints_W, np.array([]), (255,0,255), 2)
	im_with_keypoints_B = cv2.drawKeypoints(mask_B, keypoints_B, np.array([]), (255,0,255), 2)

	cv2.imshow("Final", np.hstack([im_with_keypoints_W, im_with_keypoints_B]))
    
	# Trimite prin OSC catre Max locatiile pieselor albe
	if(len(white_on) > 0):
		client.send_message("/white", white_on)

	# Trimite prin OSC catre Max locatiile pieselor negre
	if(len(black_on) > 0):
		client.send_message("/black", black_on)

    # Exit
	if cv2.waitKey(1000) & 0xFF == ord('q'):
		break 

# Clean up
cap.release()
cv2.destroyAllWindows()
