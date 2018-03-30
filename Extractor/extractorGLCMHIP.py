import cv2,numpy
from skimage.feature import greycomatrix,greycoprops
def extractor(image,winSize):
    """ image is Numpy type submatrix from an photograph.
    winSize is an odd number for size of the patch.

    This returns a feature vector with GCLM paramas for each point i.e. matrix
    """

    # Finding Harris's Intrest Points,
    w = int(winSize/2)
    pad = [w,image.shape[0]-w-1,w,image.shape[1]-w-1]

    img=image[pad[0]:pad[1],pad[2]:pad[3]].copy()
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
    ret = True
    if len(z)<10:
        ret = False
    z=z[:10]

    #Finding features
    features = []
    for x,y in z:
        patch = image[y-w:y+w+1,x-w:x+w+1]
        glcm = greycomatrix(patch, [5], [0], 256, symmetric=True, normed=True)
        features.append(greycoprops(glcm, 'contrast')[0, 0])
        features.append(greycoprops(glcm, 'dissimilarity')[0, 0])
        features.append(greycoprops(glcm, 'homogeneity')[0, 0])
        features.append(greycoprops(glcm, 'energy')[0, 0])
        features.append(greycoprops(glcm, 'correlation')[0, 0])
    
    return ret,numpy.array(features)
if __name__ == '__main__':
    import time
    image = cv2.imread('test2.jpeg')
    image = cv2.cvtColor(image[:150,:150],cv2.COLOR_RGB2GRAY)
    image = extractor(image,13)        
    print(image)
