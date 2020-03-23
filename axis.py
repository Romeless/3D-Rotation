from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open("sample.jpg"))
print(img.shape)
img = img / img.max()

def axis_rotate(planeX, planeY, planeZ, angle, order="XYZ"):
    order_arr = list(order)
    
    for i, plane in enumerate(order_arr):
        if plane == "X":
            print("PLANE X")
            A = get_rotation(angle[i])
            planeY, planeZ = axis_rotate_next(planeY, planeZ, A)
        elif plane == "Y":
            print("PLANE Y")
            A = get_rotation(angle[i])
            planeX, planeZ = axis_rotate_next(planeX, planeZ, A)
        elif plane == "Z":
            print("PLANE Z")
            A = get_rotation(angle[i])
            planeX, planeY = axis_rotate_next(planeX, planeY, A)
        else:
            print("ORDER WRONG")
            exit()
    
    return planeX, planeY, planeZ

def axis_rotate_next(plane1, plane2, matrix):
    new_plane_1 = np.zeros(plane1.shape)
    new_plane_2 = np.zeros(plane2.shape)
    
    for xx in range(plane1.shape[0]):
        for yy in range(plane1.shape[1]):
            XY1 = np.array([plane1[xx,yy],plane2[xx,yy],1])
            
            new_XY1 = np.array(matrix @ XY1)
            new_XY1 = new_XY1 / new_XY1[2]
            
            #print(XY1, new_XY1)
            
            try:
                new_plane_1[xx,yy] = new_XY1[0]
                new_plane_2[xx,yy] = new_XY1[1]
            except IndexError:
                print("INERR")
        
    return np.round(new_plane_1,decimals=8), np.round(new_plane_2,decimals=8)

def get_rotation(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), np.sin(angle), 0],
        [-np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

X, Y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
# A blank, straight 0 Z coordinate
Z = np.zeros(X.shape)

#neoX, neoY, neoZ = axis_rotate(X, Y, Z, angle=[90], order="X")
#neoX1, neoY1, neoZ1 = axis_rotate(neoX, neoY, neoZ, angle=[90], order="Y")
#neoX2, neoY2, neoZ2 = axis_rotate(neoX1, neoY1, neoZ1, angle=[90], order="Z")

neoX, neoY, neoZ = axis_rotate(X, Y, Z, angle=[90,90,90], order="XYZ")

test = '''
fig = plt.figure()#figsize=plt.figaspect(3))
_, axarr = plt.subplots(nrows=2,ncols=2)#(projection='3d')
ax = fig.add_subplot(2,2,1, projection='3d')
ax.plot_surface(X, Y, Z, facecolors=img)
ax = fig.add_subplot(2,2,2, projection='3d')
ax.plot_surface(neoX, neoY, neoZ, facecolors=img)
ax = fig.add_subplot(2,2,3, projection='3d')
ax.plot_surface(neoX1, neoY1, neoZ1, facecolors=img)
ax = fig.add_subplot(2,2,4, projection='3d')
ax.plot_surface(neoX2, neoY2, neoZ2, facecolors=img)
print(neoX2)
print(neoY2)
print(neoZ2)
'''
plt.figure()
ax = plt.gca(projection='3d')
ax.plot_surface(X, Y, Z, facecolors=img)
plt.figure()
ax = plt.gca(projection='3d')
ax.plot_surface(neoX, neoY, neoZ, facecolors=img)
plt.show()