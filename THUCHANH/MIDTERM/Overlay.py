
import cv2
import numpy as np

img1 = cv2.imread("C:/Tap/BaoMatThongTin/file_to_encrypt_A.png")
img2 = cv2.imread("C:/Tap/BaoMatThongTin/file_to_encrypt_B.png")


dst = cv2.addWeighted(img1, 0.9, img2, 0.9, 0)

#cv2.imshow('Input Images',img1)
#cv2.imshow('Input Images',img2)
cv2.imshow('Blended Image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#file_to_encrypt.png