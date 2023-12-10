
import cv2

cap = cv2.VideoCapture (0)

while True :
    _ , fram = cap.read ()

    cv2.imshow ("Webcam Filter" , fram)
    if cv2.waitKey (25) & 0xFF == ord("q") :
        # cv2.imwrite ("output_images\outout_3.jpg" , fram)
        break