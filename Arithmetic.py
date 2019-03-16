

import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath1 =  "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png" 
    #Taken same images for both img1,img2(For different image take images of similar dimensions)
    imgpath2=   "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"

    img1=cv2.imread(imgpath1,1)    
    img2=cv2.imread(imgpath2,1)
    
    
    add=img1+img2
    sub1=img1-img2
    sub2=img2-img1
    
    titles = ['Pepper Gray', 'Peppers Color','Addition','Subtraction1','Subtraction2']
    images = [img1, img2,add,sub1,sub2]
    
    for i in range(5):
        plt.subplot(1, 5, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()