import cv2

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    filename = 'File Path where the output is to be stored'
    cap = cv2.VideoCapture(filename)
    
    
    while (cap.isOpened()):
    
        ret, frame = cap.read()
        
        print(ret)
        
        if ret:
            cv2.imshow(windowName, frame)
            if cv2.waitKey(17) == 27:
                break
        else:
            break

    cv2.destroyAllWindows()    
    cap.release()

if __name__ == "__main__":
    main()