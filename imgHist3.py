import matplotlib.pyplot as mlt
import cv2 as cv

def main():
    img = cv.imread('4.1.01.tiff',0)

    out1 = cv.equalizeHist(img)

    #clache = cv.createCLAHE()
    clache = cv.createCLAHE(clipLimit=50, tileGridSize=(8,8))
    out2 = clache.apply(img)

    images = [img,out1,out2]
    titles = ['org','adjusted histogram','CLAHE']

    for i in range(3):
        mlt.subplot(1,3,i+1)
        mlt.imshow(images[i], cmap='gray')
        mlt.title(titles[i])
        mlt.xticks([])
        mlt.yticks([])
    mlt.show()

    for i in range(3):
        mlt.subplot(1,3,i+1)
        mlt.hist(images[i].ravel(),256,[0,255])
        mlt.title(titles[i])
    mlt.show()

if __name__ == "__main__":
    main()

