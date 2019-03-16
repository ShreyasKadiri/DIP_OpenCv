import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt


def main():
    imgpath =  "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png" 

    img=cv2.imread(imgpath,0)
    
    blocksize=203
    constant=2
    th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blocksize,constant)
    th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blocksize,constant)

    
    output = [img,th1,th2]
    
    titles = ['Original', 'Mean Adaptive','Gaussian Adaptive']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(output[i],cmap="gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show() 
    
    
if __name__=="__main__":
    main()