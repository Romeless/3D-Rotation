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

### Euler Angle Rotation
This is what I understand of Euler Angle rotation by reading the module, [this video](https://www.youtube.com/watch?v=zjMuIxRvygQ) and [this other video](https://www.youtube.com/watch?v=wg9bI8-Qx2Q):

It's a rotation which rotate the object plane by plane, for example the rotation of XYX would rotate the object along the plane X, plane Y, then plane X again. However, the rotation matrix uses all 3 coordinate directly. The matrix used are different for each plane. Also, each matrix would not change the coordinate of the plane they are rotating. For example, rotating an object along the plane X would only rotate/change the Y coordinate and Z coordinate of the object.

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

Axis Rotation is a rotation that rotates only 1 plane/axis at a time, similar to Euler Angle. However, the difference is, when a plane is being rotated, that plane is outright being **ignored** rather than **not being changed** (Euler). For example, if in a 3D object, 1 plane is removed from the picture, said object is downgraded to being a 2D object. Then, said 2D object is rotated similar to how 2D rotation works. After the rotation is complete, the third plane is added back to the object, returning it back into 3D.

The matrix used for this rotation is the same as the matrix used in 2D rotation and Euler Angle's Z rotation:

```
[np.cos(angle), -np.sin(angle), 0],
[np.sin(angle), np.cos(angle), 0],
[0, 0, 1]
```

Or, maybe, I'm just misinterpretating stuff and Axis rotation and Euler rotation is the same one rotation. What matters is both worked.
