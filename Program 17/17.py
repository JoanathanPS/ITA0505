import cv2
image = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
watermark = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg") # Reuse sample.jpg as watermark for demo
h, w = watermark.shape[:2]
roi = image[0:h, 0:w]
result = cv2.addWeighted(roi, 0.7, watermark, 0.3, 0)
image[0:h, 0:w] = result
cv2.imshow("Watermarked Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()