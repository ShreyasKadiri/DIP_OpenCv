import pandas as pd
import numpy as np
import cv2



def main():
    img1=  np.zeros((512,512,3),np.uint8)
  
    cv2.line(img1,(0,99),(99,0),(255,0,0),2)
    cv2.rectangle(img1,(45,50),(100,345),(0,0,255),20)
   
    
    cv2.imshow('Image',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindow('Image')
    
if __name__ == "__main__":
    main()
