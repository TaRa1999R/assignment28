
import cv2

cap = cv2.VideoCapture (0)

while True :
    _ , fram = cap.read ()

    cv2.imshow ("Webcam Filter" , fram)
    if cv2.waitKey (25) & 0xFF == ord ("1") :
        print ("one")
        # cv2.imwrite ("output_images\outout_3_stiker.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("2") :
        print("two")
        # cv2.imwrite ("output_images\outout_3_glasses&lips.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("3") :
        print ("three")
        # cv2.imwrite ("output_images\outout_3_chessboard.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("4") :
        print ("four")
        # cv2.imwrite ("output_images\outout_3_mirror.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("q") :
        break