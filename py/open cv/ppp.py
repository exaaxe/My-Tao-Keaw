import cv2
import numpy as np
import urllib
url = r'http://www.mywebsite.com/abc.jpg'
req = urllib.request.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr,-1)
cv2.imshow('abc',img)