import cv2
img = cv2.imread("image/boy.jpg")

#show image
cv2.imshow("where is where where",img)
cv2.waitKey(5000) #ms
cv2.destroyAllWindows()