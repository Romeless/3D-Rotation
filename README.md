# Sistem Pakar Assignment 1 Task 2
#### Rama Lesmana
#### 1313617011
#### State University of Jakarta



My solution to Task 2 of Assignment 1 from class "Sistem Pakar".
This task involves the rotation of 3D object / array

Python with matplotlib 3d support is the chosen programming language used to replicate the rotation of the 3D array.


## 3D Rotation
The rotation I am being tasked to experiment on are as follow:
1. Euler Angle
2. Axis
3. Quarternion

Out of the 3, I have yet managed to implement a working Quarternion rotation.

### Original Image
![Original](/examples/true.png)

### Euler Angle Rotation
This is what I understand of Euler Angle rotation by reading the module, [this video](https://www.youtube.com/watch?v=zjMuIxRvygQ) and [this other video](https://www.youtube.com/watch?v=wg9bI8-Qx2Q):

It's a rotation which rotate the object plane by plane, for example the rotation of XYX would rotate the object along the plane X, plane Y, then plane X again. However, the rotation matrix uses all 3 coordinate directly. The matrix used are different for each plane. Also, each matrix would not change the coordinate of the plane they are rotating. For example, rotating an object along the plane X would only rotate/change the Y coordinate and Z coordinate of the object.


![Rotation X 90](/examples/euler1.png) ![Rotation Y 90](/examples/euler2.png) ![Rotation Z 90](/examples/euler3.png)

Above are the rotation of XYZ, step-by-step each 90 degrees of angle from the source image
```
[1, 0, 0],
[0, np.cos(angle), -np.sin(angle)],
[0, np.sin(angle), np.cos(angle)]
For X angle

[np.cos(angle), 0, np.sin(angle)],
[0, 1, 0],
[-np.sin(angle), 0, np.cos(angle)]
For Y angle

[np.cos(angle), -np.sin(angle), 0],
[np.sin(angle), np.cos(angle), 0],
[0, 0, 1]
For Z angle
```
According to my sources the angles are suppossed to be called *alpha*, *beta*, and *gamma* respectively but I don't think that matters in a code

The transformation are performed by doing a dot product of the rotation matrix and a homography coordinate of [x,y,z] for each point. Of course, as mentioned above, the coordinate of the plane being rotated would not be affected by the rotation, as can be seen in the matrix of each plane above. Each of them has 1 plane that would not change whatever it is being dot producted to (similar to identity matrix).

### Axis Rotation

Honestly, I don't quite get what is supposed to be Axis Rotation, however, this is my interpretation:

Axis Rotation is a rotation that rotates only 1 plane/axis at a time, similar to Euler Angle. However, the difference is, when a plane is being rotated, that plane is outright being **ignored** rather than **not being changed** (Euler). For example, if in a 3D object, 1 plane is removed from the picture, said object is downgraded to being a 2D object. Then, said 2D object is rotated similar to how 2D rotation works. After the rotation is complete, the third plane is added back to the object, returning it back into 3D. For visualization, please look at the image below

![True Above View](/examples/true_above.png) ![Z Rotated Above View](/examples/axis_z_45_above.png)

The first image above are what the original object looked from a close top-down view, removing the Z angle from equation. The second image are what the object looked from top down after the object is being rotated Z-wise 45 degree. The X and Y coordinates act similarly to 2D rotation. The Z coordinates are not changed because its rotated Z-wise. Now, for the result looked normally:

![Z Rotated](/examples/axis_z_45.png)

The matrix used for this rotation is the same as the matrix used in 2D rotation and Euler Angle's Z rotation:

```
[np.cos(angle), -np.sin(angle), 0],
[np.sin(angle), np.cos(angle), 0],
[0, 0, 1]
```

Usage and result-wise, this method is not very different from Euler Angle rotation. If one want to rotate the object multiple times with different planes, then the order of rotation needs to be specified (similar to Euler, XYZ means X first, Y second, and Z last).

Or, maybe, I'm just misunderstanding stuff and Axis rotation and Euler rotation are the same one rotation. What matters is both worked.

## How they are translated into code

### Euler

First, get all points of the object in the form of homgraphy coordinate [x,y,z]
As the object is an Image in the form of surface object, each plane (X,Y,Z) is a 2D array that stores the coordinate (instead of color like RGB value).
The coordinate can be accessed row by row and column by column of each plane.

```
new_X, new_Y, new_Z = np.zeros(X.shape), np.zeros(Y.shape), np.zeros(Z.shape)

for row in range(X.shape[0]):
  for col in range(X.shape[1]):
    new_X_coord, new_Y_coord, new_Z_coord = np.array([X[row,col], Y[row,col], Z[row, col]])
```

Next, for each rotation wanted, dot product the matrix with the homography coordinate. For example, if we want to rotate it XYX, then we would need to multiply it three times across X axis, Y axis, and X axis again before storing the new coordinates

```
    for matrix in matrices:
      new_X_coord, new_Y_coord, new_Z_coord = matrix @ np.array([newX, newY, newZ])
      
    new_X[row,col], new_Y[row,col], new_Z[row,col] = new_X_coord, new_Y_coord, new_Z_coord
 
return new_X, new_Y, new_Z
```

### Axis

The transform/rotate function of axis rotation is not very different from a 2D transform function.  Half of the code is the function of splitting 

## Interesting things I found while experimenting

One thing I found interesting in my experiment is how Python or the numbers itself aren't 100% accurate. This can be seen in the rotation of XYZ each by 90 degrees of angle.

![A mess of rotation](/examples/mess.png)

As can be seen, the values hover around 0.00e-31 to 8.00e-31 which means, outside of the first 31 decimals, they are practically the same number. However, the plotting is so accurate this very small difference looks like a big mess. This problem is fixed by rounding the values to the first n amount of decimals, I choose 8.

```    return np.round(new_plane_1,decimals=8), np.round(new_plane_2,decimals=8)```

![Rotation Z 90](/examples/euler3.png) This will fix the problem and produces the pic on the left

