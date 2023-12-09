
import cv2

cats_image = cv2.imread ("input_images\input_2.jpg")
cats_gray = cv2.cvtColor (cats_image , cv2.COLOR_BGR2GRAY)

cat_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml")
cats = cat_detector.detectMultiScale (cats_gray)
for cat in cats :
    x , y , w , h = cat
    cv2.rectangle (cats_image , (x , y) , (x + w , y + h) , (150 , 0 , 150) , 3)

cv2.imshow ("Cat Detection" , cats_image)
cv2.waitKey ()
cv2.imwrite ("output_images\outout_2.jpg" , cats_image)