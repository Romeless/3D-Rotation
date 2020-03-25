from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open("sample.jpg"))
print(img.shape)
img = img / img.max()

def transform(XYZ, nx, angle):
    new_XYZ = np.zeros(XYZ.shape)

    magnitude = np.linalg.norm(nx)
    nx = nx / magnitude
    matrix = R(get_v(nx[0], nx[1], nx[2]), angle)

    #print("magnitude: ", magnitude)
    #print("nx new: ", nx)
    #print("matrix: ", matrix)
    
    
    new_X, new_Y, new_Z = np.zeros(XYZ[0].shape), np.zeros(XYZ[1].shape), np.zeros(XYZ[2].shape)
    for row in range(XYZ[0].shape[0]):
        for col in range(XYZ[0].shape[1]):
            #print(np.array([X[row,col], Y[row,col], Z[row, col]]))
            Xx, Yy, Zz = matrix @ np.array([X[row,col], Y[row,col], Z[row, col]])

            new_X[row,col], new_Y[row,col], new_Z[row,col] = Xx, Yy, Zz 
    return np.array([new_X, new_Y, new_Z])

def R(n, angle):
    return np.eye(3) + np.sin(angle) * n + (1 - np.cos(angle)) * (np.power(n,2))

def get_v(x, y, z):
    return np.array([
        [0,-z,y],
        [z,0,-x],
        [-y,x,0]
    ])

X, Y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
# A blank, straight 0 Z coordinate
Z = np.zeros(X.shape)

nx, ny, nz = 0.5,0.5,0.5
angle = 90

neoXYZ = transform(np.array([X,Y,Z]), np.array([nx,ny,nz]), angle)

plt.figure(figsize=(5,5))
ax = plt.gca(projection='3d')
ax.plot_surface(X, Y, Z, facecolors=img)
ax.set_title("Original Image")

plt.savefig("result/original.png")

plt.figure(figsize=(5,5))
ax = plt.gca(projection='3d')
ax.plot_surface(neoXYZ[0], neoXYZ[1], neoXYZ[2], facecolors=img)
ax.set_title("after Rotation nx = [{},{},{}] angle = {}".format(nx, ny, nz, angle))

plt.savefig("result/after_quarter.png")
plt.show()