import cv2
import matplotlib.pyplot as plt

def main():
    
    impath1 ="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"
    impath2 ="C:\Shreyas\OpenCv\DIP_OpenCV\lena.png"

    img1 = cv2.imread(impath1, 0)
    img2=cv2.imread(impath2,0)
      
    plt.subplot(1, 2, 1)
    plt.imshow(img1, cmap='gray')
    plt.title('Image One')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    plt.hist(img1.ravel(), 256, [0, 255])
    plt.title('Histogram One')
    plt.xlim(xmin=0, xmax=256)
    plt.show()
    
    
    
    #For the second image
    plt.subplot(1, 2, 1)
    plt.imshow(img2, cmap='gray')
    plt.title('Image Two')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    plt.hist(img2.ravel(), 256, [0, 255])
    plt.title('Histogram Two')
    plt.xlim(xmin=0, xmax=256)
    plt.show()

if __name__ == "__main__":
    main()