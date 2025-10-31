import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    image = cv2.imread(image_path)
    color_channels = ('b', 'g', 'r')
    plt.figure(figsize=(10,5))
    for i, color in enumerate(color_channels):
        hist = cv2.calcHist([image], [i], None, [256], [0,256])
        plt.plot(hist, color=color, label=f"{color.upper()} Channel")
        plt.xlim([0,256])
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

analyze_histogram(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
