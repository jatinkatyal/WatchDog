import cv2,numpy

def extractor(image,winSize):
    """ image is Numpy type submatrix from an photograph.
    winSize is an odd number for size of the patch.

    This returns a feature matrix with a vector of size 8 for each point i.e. matrix
    """

    # Finding Harris's Intrest Points,
    w = int(winSize/2)
    pad = [w,image.shape[0]-w-1,w,image.shape[1]-w-1]

    img=image[pad[0]:pad[1],pad[2]:pad[3]]
    dst = cv2.cornerHarris(img,2,3,0.04)
    img[dst>0.01*dst.max()]=0
    y,x = numpy.where(img==0)
    z=[x,y]

    z = numpy.array(z)
    z = numpy.transpose(z)
    p = [[dst[y,x],x,y] for x,y in z]
    p.sort()
    z = [[x,y] for d,x,y in p if x>int(winSize/2) and x<image.shape[1]-int(winSize/2) and y>int(winSize/2) and y<image.shape[0]-int(winSize/2)]
    #if len(z)<10:
    #   return None
    z=z[:10]
    #Finding features at HIPs
    feature = []
    #print(image)
    for x,y in z:
        patch=image[y-w:y+w+1,x-w:x+w+1]
        matA=patch[:w+1,:w+1].copy()
        matB=patch[:w+1,w:].copy()
        matC=patch[w:,:w+1].copy()
        matD=patch[w:,w:].copy()
        a = abs(matA-matB)
        b = abs(matC-matD)
        c = abs(matA-matC)
        d = abs(matB-matD)
        for j in [a,b,c,d]:
            feature.append(numpy.mean(j))
            feature.append(numpy.std(j))
    return numpy.array(feature)

if __name__ == '__main__':
    img = cv2.imread('test.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    print('extracting features')
    a = extractor(img,5)
    numpy.savetxt('feartures.csv',a,delimiter=',')
    print(a)
    '''import time
    time.sleep(3)
    cv2.destroyAllWindows()'''