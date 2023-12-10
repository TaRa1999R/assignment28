
import cv2

my_image = cv2.imread ("input_images\input_3.jpg")
my_gray = cv2.cvtColor (my_image , cv2.COLOR_BGR2GRAY)

# 1- PANDA FILTER
face_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
faces = face_detector.detectMultiScale (my_gray)
panda_stiker = cv2.imread ("input_images\stiker_panda.png")

for face in faces :
    x , y , w , h = face
    cv2.resize (panda_stiker , (w , h))
    # my_image[x:x+w , y:y+h] = panda_stiker
    # cv2.rectangle(my_image, (x , y) , (x+w , y+h) , (150 , 0 , 150) , 2)

cv2.imshow ("Filter" , panda_stiker)
cv2.waitKey ()
# cv2.imread ("output_images\outout_3.jpg")