import cv2

# src = cv2.imread("../img/OpenCV_Logo.png", cv2.IMREAD_GRAYSCALE)
src = cv2.imread("../img/OpenCV_Logo.png", cv2.IMREAD_COLOR)

cv2.namedWindow("src", flags=cv2.WINDOW_FREERATIO)  # src 이름 창을 생성해라(생략가능)
# cv2.resizeWindow("src", 400, 200)
cv2.resizeWindow("src", 400, 300)                   #src 너비=400, 높이=300
cv2.imshow("src", src)                              #src창에 src를 출력
cv2.waitKey(0)                                      #0이면 무한대기
cv2.destroyWindow("src")                            # src창을 없애라