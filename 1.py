
import cv2
import numpy as np

football_pitch = cv2.imread ("input images\input_3.jpg")
# np.ones ((360 , 510) , dtype= np.uint8) * 255
light_green = cv2.rectangle(football_pitch, (10 , 10) , (500 , 350) , (0 , 255 , 0) , 2)

cv2.imshow ("Football Pitch" , football_pitch)
cv2.waitKey()