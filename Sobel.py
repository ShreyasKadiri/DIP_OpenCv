import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath ="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    
    
    edgesx=cv2.Sobel(img,-1,dx=1,dy=0,ksize=11,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
    edgesy=cv2.Sobel(img,-1,dx=0,dy=1,ksize=11,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
    edges=edgesx+edgesy
    
    
    titles=["Image",  "dx=1 and dy=0","dx=0 and dy=1","Edges"]
    images=[img,edgesx,edgesy,edges]
    
    
    

    for i in range(4):
        plt.subplot(2,2,1+i)
        plt.imshow(images[i],cmap="gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    
    
if __name__ == "__main__":
    main()