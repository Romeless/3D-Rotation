# Parts which come from other sources
- *.py: Drawing the Image to a 3D surface is a code I took from: https://stackoverflow.com/questions/30211049/how-to-plot-an-image-file-on-a-3d-graph-surface-using-python-not-plotting-as
I understand it's not necessary to make the object an Image but this is what interest me

- euler.py: Parts of the code in the function [euler_rotate] and also the matrix (which I re-check later through web search) is a result of discussion with [Luthfi](https://github.com/LLuthfiY). I was making sure that I understood the difference between Euler and Axis correctly. Note: I was doing Axis Rotation first and called it Euler because I thought it was Euler Rotation

# Parts I wrote myself

- I declare that every part of the code not listed above, I wrote it myself.

- axis.py: The function [euler_rotate_next] is a modified version my [2d transform](https://github.com/Romeless/Affine-2D-Transformation) code. Since I completely misunderstand how to do the rotation. ~~Since, from what I understand, rotating 1 plane of a 3D array is not so different from rotating a 2D array.~~
