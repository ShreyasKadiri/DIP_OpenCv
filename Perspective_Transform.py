import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    
    imgpath1 ="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    point1 = np.float32([[0, 0], [400, 0], [0, 400],[400,400]])
    point2 = np.float32([[0, 0], [300, 0], [0, 300],[300,300]])
    
    P = cv2.getPerspectiveTransform(point1, point2)
    
    print(P)
    
    
    output = cv2.warpPerspective(img1, P, (100, 100))
    #If the above values are reduced then it zooms in
    
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()

if __name__ == "__main__":
    main()