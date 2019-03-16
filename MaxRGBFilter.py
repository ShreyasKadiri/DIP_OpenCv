import cv2
import numpy as np

def main():
    
    w = 8000
    h = 6000
    
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
    
        (B, G, R) = cv2.split(frame)
 
        M = np.maximum(np.maximum(B, R), G)
        R[R < M] = 0
        G[G < M] = 0
        B[B < M] = 0

        output = cv2.merge((R, G, B))
    
        cv2.imshow("Original", output)

        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()