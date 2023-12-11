
import cv2

cap = cv2.VideoCapture (0)
stiker = cv2.imread ("input_images\stiker_panda.png")
glaases = cv2.imread ("input_images\stiker_glasses.png")
lips = cv2.imread ("input_images\stiker_lips.png")
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
        global w_face
        x_face , y_face , w_face , h_face = face
        # my_face = fram[x_face : x_face + w_face , y_face : y_face + h_face]
        # small_stiker = cv2.resize (stiker , [w_face , h_face])
        # fram[y_face : y_face + h_face , x_face : x_face + w_face] = small_stiker
        for eye in eyes :
            x_eye , y_eye , w_eye , h_eye = eye
            small_glasses = cv2.resize (glaases , [w_face , h_eye] )
            fram [y_eye : y_eye + h_eye , x_eye : x_eye + w_face] = small_glasses


    for lip in lips :
        x_lip , y_lip , w_lip , h_lip = lip
        # cv2.rectangle(fram , [x_lip , y_lip] , [x_lip + w_lip , y_lip + h_lip] , (150,0,150) , 2)
        # small_lip = cv2.resize (lips , [w_lip , h_lip])
        # fram [y_lip :y_lip + h_lip , x_lip : x_lip + w_lip] = small_lip

    # for eye in eyes :
        # x_eye , y_eye , w_eye , h_eye = eye
        # small_glasses = cv2.resize (glaases , [w_face , h_eye] )
        # fram [y_eye : y_eye + h_eye , x_eye : x_eye + w_face] = small_glasses

    cv2.imshow ("Webcam Filter" , fram)
    if cv2.waitKey (25) & 0xFF == ord ("q") :
        break