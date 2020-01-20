# Rubik
A Python implementation of a 3x3 Rubik cube.

Each cube state is represented as 6 arrays, one for each face. 

Looking at the cube where the red face (the side where the center color is red) is pointing at the user, and the white face is pointed upwards, the indexing for the red face goes from left to right, top to bottom.

Rotate the cube once to the left, so that the blue face is facing the user. Again, indexing goes from left to right, top to bottom.

Rotating the cube once again, the same applies for the orange face.

With the orange side facing the user, flip the cube towards you, then rotate counterclockwise. The indexing will again go from left to right, top to bottom. Rotate the cube from top to bottom instead of left to right to access the rest of the faces.
