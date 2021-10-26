import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8, maxHands=2)


while True:
    success, img = cap.read()
    #img = cv2.flip(img, 1)
    img =detector.findHands(img)


    cv2.rectangle(img, (100,100), (300,300), (255,0,255), cv2.FILLED)

    # if hands:
    #     #Hand 1
    #     hand1 = hands[0]
    #     lmList1 = hand1["lmList"] # List of 21 landmarks points
    #     bbox1 = hand1["bbox"] # bouunding box info x,y, w, h
    #     centerPoint1 = hand1["center"] #center of the hand cx, cy
    #     handType1 = hand1["type"]
    #     print(len(lmList1), lmList1)
    #     print(bbox1)
    #     print(centerPoint1)
    #     print(handType1)



    cv2.imshow("Image", img)
    cv2.waitKey(1)

