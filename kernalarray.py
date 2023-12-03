import matplotlib.pyplot as mlt
import random
import numpy as np
import cv2 as cv

def main():
    img = cv.imread('download (1).jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    k = np.array(([0,0,0],[0,1,0],[0,0,0]), np.float32)
    ed = np.array(([1,0,-1],[0,0,0],[-1,0,1]), np.float32)
    sh = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), np.float32)
    bo = np.array(np.ones ((11,11) , np.float32))/121

    print(bo)
    # print(type(k))

    iden = cv.filter2D(img, -1, k)
    edge = cv.filter2D(img, -1, ed)
    sharp = cv.filter2D(img, -1, sh)
    box = cv.filter2D(img, -1, bo)

    images = [img, iden, edge,sharp,box]
    titles = ['Original', 'identity','edge','sharp','box']

    for i in range(len(images)):
        mlt.subplot(3,2,i+1)
        mlt.imshow(images[i])
        mlt.xticks([])
        mlt.yticks([])
        mlt.title(titles[i])

    mlt.show()

if __name__ == "__main__":
    main()