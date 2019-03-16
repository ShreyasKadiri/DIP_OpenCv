

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    imgpath =  "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png" 

    img = cv2.imread(imgpath, 0)
   # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    
    
    L1=cv2.Canny(img,50,300,L2gradient=False)
    L2=cv2.Canny(img,100,150,L2gradient=True)
    
    
    titles=["Image",  "L1 Form", "L2 Form"]
    images=[img,L1,L2]
    
    
    

    for i in range(3):
        plt.subplot(2,3,1+i)
        plt.imshow(images[i],cmap="gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    
    
if __name__ == "__main__":
    main()
