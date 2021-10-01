import cv2

# color image를 binary로 하면 각 rgb채널별로 binary한 후 합쳐진것이다
# 그래서 color이미지는 binary를 하지 않는다

src = cv2.imread("../img/cman.jpg", cv2.IMREAD_GRAYSCALE)

# _, binary = cv2.threshold(src, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, binary = cv2.threshold(src, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)


cv2.namedWindow("binary")
dst = cv2.resize(binary, dsize=(640, 480), interpolation=cv2.INTER_AREA)
cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()