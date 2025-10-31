import cv2
image = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
roi = image[50:150, 50:150]
image[200:300, 200:300] = roi
cv2.imshow("ROI Copied", image)
cv2.waitKey(0)
cv2.destroyAllWindows()