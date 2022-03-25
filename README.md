# Semanatec "El arte de programar"

## Miembros del equipo:
- Brenda Hernández Estrada a01368953
- Maricarmen Barillas Duarte a01369993

## Objetivo
Con el uso del leguaje de programación python realizar un código que modifiique una imagen mediante la implementación de los conceptos aprendidos en clase. Un ejemplo de estos conceptos son los Kernels. 

## Introducción
Conceptos básicos

## Qué es una convolución
Tratamiento de la colección de píxeles en coordenadas rectangulares (matriz) de una imagen por otra matriz  llamada Kernel.  Dependiendo el efecto deseado, será el kernel utilizado.

## Qué es un Kernel
Pequeña matriz que nos permite aplicar "filtros" que resaltan, alisan, detectan bordes, enfocan y más hacen más funciones en imágenes.

## Kernels utilizados
- Gaussian blur
Es un kernel de desenfoque y ayuda a reducir el ruido de una imagen. Da uso de la función gaussiana, llamada así por Carl Friderich Gauss. 
La ecuación se ve de la siguiente manera: 

![WhatsApp Image 2022-03-25 at 10 26 17 AM](https://user-images.githubusercontent.com/84739987/160161475-1d455d8a-3154-418b-96e0-06964aeaa23e.jpeg)

- Mexican Hat/Ricker wavelet
Es un kernel que desenfoca y muestra contornos. Ayuda a la imagen para que se vea mas clara. Es la segunda derivada negativa normalizada de una función gaussiana. Se ve de la siguiente manera:

![WhatsApp Image 2022-03-25 at 10 26 17 AM](https://user-images.githubusercontent.com/84739987/160162614-48daf16a-d019-4612-8982-c5351ce57032.jpeg)

## Resultado de kernels
- Kernal Exponential


![WhatsApp Image 2022-03-25 at 10 39 02 AM](https://user-images.githubusercontent.com/84739987/160163720-b3928c85-65d9-46dd-a768-fe9cc1c62306.jpeg)

- Gaussian blur


![WhatsApp Image 2022-03-25 at 10 39 02 AM (1)](https://user-images.githubusercontent.com/84739987/160163653-c8fab918-d641-43f0-8f41-c32b2305647c.jpeg)

- Mexican Hat/Ricker wavelet


![WhatsApp Image 2022-03-25 at 10 39 03 AM](https://user-images.githubusercontent.com/84739987/160163640-fed4a93d-c83f-4dc9-9484-1ee8cbf5323b.jpeg)

## Implementación
``` python
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

Is = Image.open('Tom Holland.jpeg');
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

```
