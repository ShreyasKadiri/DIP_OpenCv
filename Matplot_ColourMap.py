#Matplots and colormaps
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
    
    
    imgpath="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img=cv2.imread(imgpath,0)
    
    #Modi in red
    plt.imshow(img,cmap="Reds")
    #To remove the label values on x and y axis
    plt.xticks([])
    plt.yticks([])
    plt.title("Modi in Red")
    plt.show()

    
    plt.imshow(img,cmap="Blues")
    plt.xticks([])
    plt.yticks([])
    plt.title("Modi by default")
    plt.show()
    
    
    
    
    
    
   # cv2.imshow('Modi',img)
   # cv2.waitKey(0)
   # cv2.destroyAllWindow('Modi')
    
if __name__ == "__main__":
    main()