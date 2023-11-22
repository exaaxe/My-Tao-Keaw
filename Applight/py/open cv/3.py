import cv2
img = cv2.imread("image/boy.jpg")
imgresize = cv2.resize(img,(400,400))

#show image
cv2.imshow("where is where where",imgresize)
cv2.waitKey(5000) #ms
cv2.destroyAllWindows()