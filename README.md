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

### Original Image
![Original](/images/original.png)

### Euler Angle Rotation
This is what I understand of Euler Angle rotation by reading the module, [this video](https://www.youtube.com/watch?v=zjMuIxRvygQ) and [this other video](https://www.youtube.com/watch?v=wg9bI8-Qx2Q):

It's a rotation which rotate the object plane by plane, for example the rotation of XYX would rotate the object along the plane X, plane Y, then plane X again. However, the rotation matrix uses all 3 coordinate directly. The matrix used are different for each plane. Also, each matrix would not change the coordinate of the plane they are rotating. For example, rotating an object along the plane X would only rotate/change the Y coordinate and Z coordinate of the object.


![Rotation X 90](/images/euler_x.png) ![Rotation Y 90](/images/euler_y.png) ![Rotation Z 90](/images/euler_z.png)

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

Axis rotation uses Rodriguez formula to calculate the matrix transformation. This rotation rotates along a new (x,y,z) axis, and an angle value is needed to set how far the rotation will go. To use this method, the value of the axis needs to be specified, meaning this method needs 4 values: x rotation, y rotation, z rotation, and angle

Rodriguez formula = ```I + sin(theta) * n + (1 - cos(theta) * n ** 2)```

This formula produces a 3x3 transfomation matrix to be multiplied by 

### Unit Quarternion

I don't completely understand the logic behind this method, what I understand is this method represent the rotation of an object to 4 component vector (x, y, z, w). How this method works is to use the first 3 component (x,y,z) to create a 3x3 matrix v which is:
```
[0,-z,y]
[z,0,-x]
[-y,x,0]
```

Then, with a modified Rodriguez formula, a transformation matrix can be calculated:
```
R = I + 2 w * v + 2 v ** 2

which result in

R = [1 - 2 * (y**2 + z**2), 2 * (x * y - z * w), 2 * (x * z + y * w)]
    [2 * (x * y + z * w), 1 - 2 * (x**2 + z**2), 2 * (y * z - x * 2)]
    [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x**2 + y**2)]
```

This transformation matrix can then be dot produt to the homography coordinate (x,y,z)

The difference between this method and axis rotation is this rotation can be represented into a quarternion unit (q) and be merged with another quarternion unit to merge rotations.

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

This method take 3 values of nx, ny, and nz, which translate to where the rotation will go, and angle, which translate to how far the rotation will go.

```
def R(n, angle):
    return np.eye(3) + np.sin(angle) * n + (1 - np.cos(angle)) * (np.power(n,2))

def get_v(x, y, z):
    return np.array([
        [0,-z,y],
        [z,0,-x],
        [-y,x,0]
    ])
```

These two function will generate a matrix R which is used to transform the original coordinate to a new coordinate
```
    new_X, new_Y, new_Z = np.zeros(XYZ[0].shape), np.zeros(XYZ[1].shape), np.zeros(XYZ[2].shape)
    for row in range(XYZ[0].shape[0]):
        for col in range(XYZ[0].shape[1]):
            #print(np.array([X[row,col], Y[row,col], Z[row, col]]))
            Xx, Yy, Zz = matrix @ np.array([X[row,col], Y[row,col], Z[row, col]])

            new_X[row,col], new_Y[row,col], new_Z[row,col] = Xx, Yy, Zz 
    return np.array([new_X, new_Y, new_Z]
 ```
 
### Unit Quarternion

Similar to Axis rotation, this method takes 3 value of axis rotation and another value for angle.

Difference is how the matrix is calculated:
```
v = get_v(x,y,z)
    w = np.cos(angle/2)

    return np.array(np.eye(3) + 2 * w * v + 2 * v ** 2)
```
Also this method supposedly can be merged by another quarternion rotation but I haven't implemented that yet


## Interesting things I found while experimenting

One thing I found interesting in my experiment is how Python or the numbers itself aren't 100% accurate. This can be seen in the rotation of XYZ each by 90 degrees of angle. This is caused by this line of code

```
return new_plane_1, np.round new_plane_2
```

![A mess of rotation](/images/euler_z_mess.png)

As can be seen, the values hover around 0.00e-31 to 8.00e-31 which means, outside of the first 31 decimals, they are practically the same number. However, the plotting is so accurate this very small difference looks like a big mess. This problem is fixed by rounding the values to the first n amount of decimals, I choose 8.

```
return np.round(new_plane_1,decimals=8), np.round(new_plane_2,decimals=8)
```

![Rotation Z 90](/examples/euler_z.png)

This will fix the problem and produces the pic above


## Axis / Quarternion
Another thing I found interesting is how Axis / Quarternion are basically just the same type of calculation, just differently represented. Quarternion can be represented by a 4 vector (x,y,z,w), just this 4 value can determine where the rotation will go. Another different is Quarternion ability to be merged but I haven't tried that one yet.
