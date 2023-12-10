
import cv2

cap = cv2.VideoCapture (0)

while True :
    _ , fram = cap.read ()
    gray_fram = cv2.cvtColor (fram , cv2.COLOR_RGB2GRAY)

    face_detectoe = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    faces = face_detectoe.detectMultiScale (gray_fram , scaleFactor = 1.3)
    eye_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_eye.xml")
    eyes = eye_detector.detectMultiScale (gray_fram , scaleFactor = 1.3)
    lip_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_smile.xml")
    lips = lip_detector.detectMultiScale (gray_fram , scaleFactor = 1.3)

    for face in lips :
        x , y , w , h = face
        cv2.rectangle (fram , (x , y) , (x + w , y + h) , (150 , 0 , 150) , 2)

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