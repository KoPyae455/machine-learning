import cv2 as cv
import numpy as np

def main():
    img = cv.imread('photo1700298794.jpeg',1)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    sobelx = cv.Sobel(img, -1,1,0, ksize=5)
    sobely = cv.Sobel(img, -1, 0, 1, ksize=5)

    laplacian = cv.Laplacian(img,-1)
    sharpening = np.array (([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)
    sharp = cv.filter2D(img, -1, sharpening)

    titles = ['Original', 'sobelx', 'sobely', 'laplacian', 'sharpen']
    images = [img, sobelx,sobely,laplacian,sharp]

    while True:
        cv.imshow('original', img)
        cv.imshow('sobel x',sobelx)
        cv.imshow('sobel y', sobely)
        cv.imshow('laplacian', laplacian)
        cv.imshow('sharpen', sharp)

        k = cv.waitKey(10)
        if k == 27:
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    

