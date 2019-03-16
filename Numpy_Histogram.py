import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img = cv2.imread(imgpath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    R, G, B = cv2.split(img)

#    plt.subplot(1, 2, 1)
#    plt.imshow(img)
#    plt.title('Image')
#    plt.xticks([])
#    plt.yticks([])
    
    plt.subplot(3, 1, 1)
    hist, bins = np.histogram(R.ravel(), 256, [0,255])
    plt.xlim([0, 255])
    plt.plot(hist, color='r')
    plt.title('Red Histogram')

    plt.subplot(3, 1, 2)
    hist, bins = np.histogram(G.ravel(), 256, [0,255])
    plt.xlim([0, 255])
    plt.plot(hist, color='g')
    plt.title('Green Histogram\n')

    plt.subplot(3, 1, 3)
    hist, bins = np.histogram(B.ravel(), 256, [0,255])
    plt.xlim([0, 255])
    plt.plot(hist, color='b')
    plt.title('Blue Histogram')    
    
    plt.show()

if __name__ == "__main__":
    main()