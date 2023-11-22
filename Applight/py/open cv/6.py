import cv2 #เปิดกล้องคอลเสว

cap = cv2.VideoCapture(0)

while (True):
    ret , frame = cap.read() #input vdo form camera
    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows

