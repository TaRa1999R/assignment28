
import cv2
import numpy as np

football_pitch = cv2.imread ("input_images\input_1.jpg")
light_green = cv2.rectangle (football_pitch, (0 , 0) , (532 , 382) , (0 , 200 , 83) , -1)
start_point = 76
for i in range (3) :
    dark_green = cv2.rectangle (football_pitch , (start_point , 0) , (start_point + 76 , 382) , (46 , 125 , 50) , -1)
    start_point += 150


cv2.imshow ("Football Pitch" , football_pitch)
cv2.waitKey()
# cv2.imwrite ("output_images\outout_1.jpg" , football_pitch)