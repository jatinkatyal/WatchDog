import cv2,numpy
from skimage.feature import greycomatrix,greycoprops
def extractor(image):
    """ image is Numpy type submatrix from an photograph.

    This returns a feature vector with GCLM paramas for each point i.e. matrix
    """

    #Finding features
    features = []
    glcm = greycomatrix(image, [5], [0], 256, symmetric=True, normed=True)
    features.append(greycoprops(glcm, 'contrast')[0, 0])
    features.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    features.append(greycoprops(glcm, 'homogeneity')[0, 0])
    features.append(greycoprops(glcm, 'energy')[0, 0])
    features.append(greycoprops(glcm, 'correlation')[0, 0])
    
    return numpy.array(features)

if __name__ == '__main__':
    import time
    image = cv2.imread('test2.jpeg')
    image = cv2.cvtColor(image[:150,:150],cv2.COLOR_RGB2GRAY)
    image = extractor(image)        
    print(image)