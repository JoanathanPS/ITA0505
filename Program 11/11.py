import cv2

image = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
flipped = cv2.flip(image, 1)
rotated = cv2.rotate(flipped, cv2.ROTATE_180)
cv2.imshow("Original Image", image)
cv2.imshow("Rotated 180 Degrees", rotated)
cv2.imwrite(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\rotated_180.jpg", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
