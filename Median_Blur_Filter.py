import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    
    imgpath ="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows,columns,channels=img.shape
    p=0.05
    noisy=np.zeros(img.shape,np.uint8)
    
    for i in range(rows):
        for j in range(columns):
            r=random.random()
            if r<p/2:
                noisy[i][j]=[0,0,0]
            elif r<p:
                noisy[i][j]=[255,255,255]
            else:
                noisy[i][j]=img[i][j]
                
    denoised=cv2.medianBlur(img,3)
                
                
                
    output=[img,noisy,denoised]
    titles=['Original', 'Noisy(Salt and Pepper Added','Denoised']
    
    
    for i in range(3):
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.show()

if __name__ == "__main__":
    main()