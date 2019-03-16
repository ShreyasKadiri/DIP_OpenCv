import cv2
import numpy as np
import time
#import matplotlib.pyplot as plt

def main():
    
   # path = "C:\Shreyas\OpenCv"
    
    imgpath1 =  "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    imgpath2 =   "C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    for i in np.linspace(0, 1,100):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        cv2.imshow('Transition', output)
        time.sleep(0.02)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()