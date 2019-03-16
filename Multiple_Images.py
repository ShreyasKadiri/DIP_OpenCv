#Displaying multiple images using matplotlib
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath1="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    imgpath2="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    
    img1=cv2.imread(imgpath1,1)    
    img2=cv2.imread(imgpath2,1)
    
    titles = ['Pepper Gray', 'Peppers Color']
    images = [img1, img2]
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()
    