import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

Is = Image.open('sudoku.png');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;

k0 = numpy.array([[0,-1,0],[-1,0,1],[0,1,0]])

'''
1 -1 1
-1 4 -1
 1 -1 1
'''

k1 = numpy.array([[0,0,0],[-1,0,1],[0,0,0]])

'''
 0 0 0
-1 0 1
 0 0 0
'''


k2 = numpy.array([[0,-1,0],[0,0,0],[0,1,0]])

'''
 0 -1 0
 0  0 0
 0  1 0
'''
def k3():
  A= numpy.zeros((3,3))
  for x in range(-1,2):
    for y in range (-1,2):
      A[x][y] = numpy.exp( -0.5* (x+y)**2 )
  return A

def k4(sigma, size):
  B= numpy.zeros((size,size))
  for a in range(-size//2,size//2 +1):
    for b in range(-size//2,size//2+1):
      B[a][b] = 1/(2*numpy.pi*sigma **2)*numpy.exp(-(a**2 + b **2)/(2*sigma**2))
  return B

def k5(sigma, size):
  C= numpy.zeros((size,size))
  for c in range(-size//2,size//2 +1):
    for d in range(-size//2,size//2+1):
      i = (c**2 + d**2/(sigma**2))
      g = (1-1/2 * i)
      h = (1/(numpy.pi*sigma**4))*(g)
      C[c][d] = ((h) * numpy.exp(-(c**2+d**2/(2*sigma**2))))
  return C

J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)
J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)
J2 = ndimage.convolve(I, k2, mode='constant', cval=0.0)
J3 = ndimage.convolve(I, k3(), mode='constant', cval=0.0)
J4 = ndimage.convolve(I, k4(15,19), mode='constant', cval=0.0)
J5 = ndimage.convolve(I, k5(3,9), mode='constant', cval=0.0)

plt.figure(figsize = (15,15))

plt.subplot(2,2,1)
plt.imshow(Is)
plt.xlabel('Input Image')

plt.subplot(2,2,2)
plt.imshow(J0)
plt.xlabel('VH direction')

plt.subplot(2,2,3)
plt.imshow(J1)
plt.xlabel('Horizontal direction')

#plt.subplot(2,2,4)
#plt.imshow(J2)
#plt.xlabel('Vertical direction')

#plt.subplot(2,2,4)
#plt.imshow(J3)
#plt.xlabel('Kernel exponencial')

#plt.subplot(2,2,4)
#plt.imshow(J4)
#plt.xlabel('Gaussian blur')

plt.subplot(2,2,4)
plt.imshow(J5)
plt.xlabel('Ricker wavelet')

plt.grid(False)
plt.show()
