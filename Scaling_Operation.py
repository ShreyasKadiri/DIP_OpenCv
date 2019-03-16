import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath =  "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img1 = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    T = np.float32([[1, 0, 150], [0, 1, 50]])
    
    print(T)
    
    
    output = cv2.warpAffine(img1, T, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()

if __name__ == "__main__":
    main()