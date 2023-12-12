
import cv2

cap = cv2.VideoCapture (0)
stiker = cv2.imread ("input_images\stiker_panda.png")
glaases = cv2.imread ("input_images\stiker_glasses.png")
stiker_lip = cv2.imread ("input_images\stiker_lips.png")
face_detectoe = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eye_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")
lip_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_smile.xml")

while True :
    _ , fram = cap.read ()
    gray_fram = cv2.cvtColor (fram , cv2.COLOR_RGB2GRAY)

    faces = face_detectoe.detectMultiScale (gray_fram , scaleFactor = 1.3)
    eyes = eye_detector.detectMultiScale (gray_fram , scaleFactor = 1.3 , minNeighbors = 20)
    lips = lip_detector.detectMultiScale (gray_fram , scaleFactor = 1.3 , minNeighbors = 35)

    for face in faces :
        x_face , y_face , w_face , h_face = face
        my_face = fram [y_face : y_face + h_face , x_face : x_face + w_face]
        cv2.rectangle (fram , (x_face , y_face) , (x_face + w_face , y_face + h_face) , (0,0,150) , 2)

    for lip in lips :
        x_lip , y_lip , w_lip , h_lip = lip
        cv2.rectangle (fram , (x_lip , y_lip) , (x_lip + w_lip , y_lip + h_lip) , (150,0,150) , 2)

    for eye in eyes :
        x_eye , y_eye , w_eye , h_eye = eye
        cv2.rectangle (fram , (x_face , y_eye) , (x_face + w_face , y_eye + h_eye) , (150,0,0) , 2)
        
    cv2.imshow ("Webcam Filter" , fram)
    if cv2.waitKey (25) & 0xFF == ord ("1") :
        small_stiker = cv2.resize (stiker , [w_face , h_face])
        fram[y_face : y_face + h_face , x_face : x_face + w_face] = small_stiker
        cv2.imshow ("Stiker on Face" , fram)
        cv2.imwrite ("output_images\outout_3_stiker.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("2") :
        small_glasses = cv2.resize (glaases , [w_face , h_eye] )
        fram [y_eye : y_eye + h_eye , x_eye : x_eye + w_face] = small_glasses
        small_lip = cv2.resize (stiker_lip , [w_lip , h_lip])
        fram [y_lip :y_lip + h_lip , x_lip : x_lip + w_lip] = small_lip
        cv2.imshow ("Glasses and Lips on Face" , fram)
        cv2.imwrite ("output_images\outout_3_glasses&lips.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("3") :
        small_face = cv2.resize (my_face , [10 , 10])
        larg_face = cv2.resize (small_face , [w_face , h_face] , interpolation = cv2.INTER_NEAREST)
        fram[y_face : y_face + h_face , x_face : x_face + w_face] = larg_face
        cv2.imshow ("Checkered Face" , fram)
        cv2.imwrite ("output_images\outout_3_chessboard.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("4") :
        mirror = cv2.flip (fram[: , fram.shape[1] // 2 : fram.shape[1]] , 1)
        fram[: , :fram.shape[1] // 2] = mirror
        cv2.imshow ("Mirror" , fram)
        cv2.imwrite ("output_images\outout_3_mirror.jpg" , fram)

    if cv2.waitKey (25) & 0xFF == ord ("q") :
        break