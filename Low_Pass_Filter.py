import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath ="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    
    
    box=cv2.boxFilter(img,-1,(53,53))
    blur=cv2.blur(img,(13,13))
    gaussian=cv2.GaussianBlur(img,(7,7),0)
    
    titles=["Image",  "Box Filter", "Blur",  "Gaussian Blur"]
    images=[img,box,blur,gaussian]
    
    
    

    for i in range(4):
        plt.subplot(2,2,1+i)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    
    
if __name__ == "__main__":
    main()