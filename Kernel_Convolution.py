import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath ="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    k=np.array(([0,1,0],
                [1,-4,1],
                [0,1,0]),np.float32)
    
    
    
    print(k)
    print(type(k))
    
    output=cv2.filter2D(img,-1,k)
    
    

    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    
    plt.subplot(1, 2, 2)
    plt.imshow(output)
    plt.title('Filtered Image')
    
    plt.show()

if __name__ == "__main__":
    main()