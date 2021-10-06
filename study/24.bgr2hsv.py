import cv2

src = cv2.imread("../img/crow.jpg")
dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()