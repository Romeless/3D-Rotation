from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open("sample.jpg"))
print(img.shape)
img = img / img.max()

def euler_rotate(X, Y, Z, angle, order):
    order_arr = np.array(list(order))
    matrix_R = []

    mapping = {"X": get_rotation_X, "Y": get_rotation_Y, "Z": get_rotation_Z}

    for i in range(len(order_arr)):
        #print(order_arr[i])
        #print(mapping[order_arr[i]])
        #print(mapping[order_arr[i]](angle[i]))
        matrix_R.append(mapping[order_arr[i]](angle[i]))
    matrix_R = np.array(matrix_R)
    #print(matrix_R)

    new_X, new_Y, new_Z = np.zeros(X.shape), np.zeros(Y.shape), np.zeros(Z.shape)
    for row in range(X.shape[0]):
        for col in range(X.shape[1]):
            #print(np.array([X[row,col], Y[row,col], Z[row, col]]))
            Xx, Yy, Zz = matrix_R[0] @ np.array([X[row,col], Y[row,col], Z[row, col]])

            for i in range(1, len(matrix_R)):
                #print(i)
                Xx, Yy, Zz = matrix_R[i] @ np.array([Xx, Yy, Zz])

            new_X[row,col], new_Y[row,col], new_Z[row,col] = Xx, Yy, Zz 
    return np.round(new_X,decimals=8), np.round(new_Y,decimals=8), np.round(new_Z,decimals=8)

    
def get_rotation_X(angle):
    angle = np.radians(angle)
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

def get_rotation_Y(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])

def get_rotation_Z(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

X, Y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
# A blank, straight 0 Z coordinate
Z = np.zeros(X.shape)

neoX, neoY, neoZ = euler_rotate(X, Y, Z, angle=[90,90,90], order="XYZ")
plt.figure()
ax = plt.gca(projection='3d')
ax.plot_surface(X, Y, Z, facecolors=img)
plt.figure()
ax = plt.gca(projection='3d')
ax.plot_surface(neoX, neoY, neoZ, facecolors=img)
plt.show()