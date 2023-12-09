
import cv2

football_pitch = cv2.imread ("input_images\input_1.jpg")
cv2.rectangle (football_pitch, (0 , 0) , (532 , 382) , (0 , 200 , 83) , -1)

start_point = 76
for i in range (3) :
    cv2.rectangle (football_pitch , (start_point , 0) , (start_point + 76 , 382) , (46 , 125 , 50) , -1)
    start_point += 150

cv2.rectangle (football_pitch , (16 , 16) , (516 , 366) , (255 , 255 , 255) , 2)
cv2.line (football_pitch , (266 , 16) , (266 , 366) , (255 , 255 , 255) , 2)

cv2.circle (football_pitch , (266 , 196) , 6 , (255 , 255 , 255) , -1)
cv2.circle (football_pitch , (266 , 196) , 46 , (255 , 255 , 255) , 2)

start_point = 16
for i in range (2) :
    cv2.rectangle (football_pitch , (start_point , 96) , (start_point + 82 , 296) , (255 , 255 , 255) , 2)
    start_point += 418

start_point = 16
for i in range (2) :
    cv2.rectangle (football_pitch , (start_point , 151) , (start_point + 27 , 241) , (255 , 255 , 255) , 2)
    start_point += 473

cv2.imshow ("Football Pitch" , football_pitch)
cv2.waitKey()
cv2.imwrite ("output_images\outout_1.jpg" , football_pitch)