import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath = "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img1 = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    R= cv2.getRotationMatrix2D((columns/2, rows/2),100, 1)
    
    print(R)
    
    
    output = cv2.warpAffine(img1, R, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()

if __name__ == "__main__":
    main()