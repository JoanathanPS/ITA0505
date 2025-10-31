import cv2

image = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Original Image", image)
cv2.imshow("Rotated 90 Degrees", rotated)
cv2.imwrite(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\rotated_90.jpg", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
