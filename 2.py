
import cv2

cats_image = cv2.imread ("input_images\input_2_3.jpeg")

cv2.imshow ("Cat Detection" , cats_image)
cv2.waitKey ()
# cv2.imwrite ("output_images\input_2.jpg")