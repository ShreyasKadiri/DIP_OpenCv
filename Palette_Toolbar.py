import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def emptyFunction():
    pass

def main():

    img=np.zeros((512,512,3),np.uint8)
    windowname="Palette Window Bar"
    cv2.namedWindow(windowname)
    
    cv2.createTrackbar('B',windowname,0,255,emptyFunction)
    cv2.createTrackbar('G',windowname,0,255,emptyFunction)
    cv2.createTrackbar('R',windowname,0,255,emptyFunction)

    
    
    while(True):
        cv2.imshow(windowname,img)
        
        if cv2.waitKey(1)==27:
            break
        
        
        blue=cv2.getTrackbarPos('B',windowname)
        green=cv2.getTrackbarPos('G',windowname)
        red=cv2.getTrackbarPos('R',windowname)
        
        img[:]=[blue,green,red]
        
        print(blue,green,red)

        

        
        
        
           
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()