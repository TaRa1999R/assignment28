
import cv2
import numpy as np

def stiker_face (img , faces) :
    for face in faces :
        xf , yf , wf , hf = face
        small_emoji = cv2.resize (emoji_stiker , [wf , hf])
        
        for i in range (hf) :
            for j in range (wf) :
                if small_emoji[i][j][0] == 0 and small_emoji[i][j][1] == 0 and small_emoji[i][j][2] == 0 :
                    small_emoji[i][j] = img[yf + i , xf + j]

        img [yf : yf + hf , xf : xf + wf] = small_emoji
    return img
    

def lip_and_eye (img , eyes , lips) :
    for lip in lips :
        xl , yl , wl , hl = lip
        small_lip = cv2.resize (lip_stiker , [wl , hl])

        for i in range (hl) :
            for j in range (wl) :
                if small_lip[i][j][0] == 0 and small_lip[i][j][1] == 0 and small_lip[i][j][2] == 0 :
                    small_lip[i][j] = img [yl + i , xl + j]
        
        img [yl : yl + hl , xl : xl + wl] = small_lip
    
    return img


def Checkered_face () :
    ...


def mirror () :
    ...

    
cap = cv2.VideoCapture (0)

emoji_stiker = cv2.imread ("input_images\stiker_cool.png")
glaases_stiker = cv2.imread ("input_images\stiker_glasses.png")
lip_stiker = cv2.imread ("input_images\stiker_lips.png")

face_detectoe = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eye_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")
lip_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_smile.xml")

while True :
    _ , fram = cap.read ()
    gray_fram = cv2.cvtColor (fram , cv2.COLOR_RGB2GRAY)

    faces = face_detectoe.detectMultiScale (gray_fram , scaleFactor = 1.3)
    eyes = eye_detector.detectMultiScale (gray_fram , scaleFactor = 1.3 , minNeighbors = 20)
    lips = lip_detector.detectMultiScale (gray_fram , scaleFactor = 1.3 , minNeighbors = 45)

    # for eye in eyes :
        # xe,ye,we,he = eye
        # cv2.rectangle (fram , (xe , ye) , (xe + we , ye + he) , (0 , 0 , 150) , 2)


    if cv2.waitKey (25) & 0xFF == ord ('1') :
        fram = stiker_face (fram , faces)
        # cv2.imwrite ("output_images\outout_3_emoji.jpg" , fram)

    elif cv2.waitKey (25) & 0xFF == ord ('2') :
        fram = lip_and_eye (fram , eyes , lips)
        # cv2.imwrite ("output_images\outout_3_glasses&lips.jpg" , fram)

    elif cv2.waitKey (25) & 0xFF == ord ('3') :
        print ("three")
        fram = Checkered_face ()
        # cv2.imwrite ("output_images\outout_3_checkred_face.jpg" , fram)

    elif cv2.waitKey (25) & 0xFF == ord ('4') :
        print ("four")
        fram = mirror ()
        # cv2.imwrite ("output_images\outout_3_mirror.jpg" , fram)

    elif cv2.waitKey (25) & 0xFF == ord ('q') :
        break

    cv2.imshow ("Webcam Filters" , fram)