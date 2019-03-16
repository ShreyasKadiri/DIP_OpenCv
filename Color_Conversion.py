#Display all the color conversion 
import cv2
def main():
    
    
    j=0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            j=j+1
        print(filename)
        
    print("There are a total of "+ str(j+1)+ "colorspaces")
    
    
    
if __name__ == "__main__":
    main()
    
    
    