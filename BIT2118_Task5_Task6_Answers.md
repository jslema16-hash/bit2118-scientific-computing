# BIT 2118 Scientific Computing: Tasks 5 and 6

---
# TASK 5: Matrix Algebra and Matrix Operations
File: `code/Task_05_matrix_algebra.py`

## B. Input values and mathematical operation
**Inputs**
- `points`: the four corners of a unit square, each row [x, y]: (0,0), (1,0), (1,1), (0,1)
- `angle`: 45 degrees (converted to radians)
- `scale`: factors 2.0 in x and 1.5 in y

**Operations**
1. Rotation matrix R = [[cos t, -sin t],[sin t, cos t]]
2. Scaling matrix S = diag(2, 1.5)
3. Combined transformation T = R @ S (matrix multiplication)
4. Transform all points: `points @ T.T` (transpose is needed because points are stored as rows)
5. Determinant det(T), which shows how area changes

**Output**

| Original | Transformed |
|---|---|
| (0, 0) | (0, 0) |
| (1, 0) | (1.414, 1.414) |
| (1, 1) | (0.354, 2.475) |
| (0, 1) | (-1.061, 1.061) |

Determinant = 3.0

## C. Change a parameter and explain
| Change | New output | Effect |
|---|---|---|
| Angle 45 to 90 degrees | (1,0)->(0,2), (1,1)->(-1.5,2), (0,1)->(-1.5,0); det = 3.0 | The shape turns to a new orientation. Area is unchanged. |
| Scale (2, 1.5) to (3, 1.5) | (1,0)->(2.121, 2.121), (1,1)->(1.061, 3.182); det = 4.5 | The shape is stretched more, and the area grows from 3 to 4.5. |

Explanation: the angle only changes the direction of the shape. The scale factors change its size. The determinant equals sx x sy (rotation always has determinant 1), so it changes only when the scale changes.

## D. Meaning of the output
The unit square (area 1) is stretched by 2 in x and 1.5 in y, then rotated 45 degrees anticlockwise. It becomes a tilted parallelogram. The origin (0,0) does not move, because a matrix transformation always keeps the origin fixed. The determinant of 3 means the new shape has 3 times the original area (2 x 1.5 = 3). It is positive, so the shape is not mirrored. Every point is transformed in the same way, which is why matrices are used in graphics and robotics.

## E. Modified program: a different real-world case
**Case:** a 6 m x 4 m rectangular room on a floor plan must be rotated 30 degrees and drawn at half size (scale 0.5) on a map.

**Assumptions**
- The origin is the bottom-left corner of the room.
- Units are metres.
- Uniform scale of 0.5 in both directions.
- The room is a perfect rectangle, and rotation is anticlockwise.

**Input data:** corners (0,0), (6,0), (6,4), (0,4); angle 30 degrees; scale (0.5, 0.5)

```python
import numpy as np

# Corners of a 6 m x 4 m room, each row is [x, y] in metres
room = np.array([[0.0, 0.0], [6.0, 0.0], [6.0, 4.0], [0.0, 4.0]])

angle = np.deg2rad(30)
rotation = np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle),  np.cos(angle)]])
scale = np.array([[0.5, 0.0],
                  [0.0, 0.5]])

transformation = rotation @ scale
map_points = room @ transformation.T

print("Room corners on the map:\n", np.round(map_points, 3))
print("Determinant:", np.linalg.det(transformation))
print("Original area:", 6 * 4, "m^2")
print("Map area:", 6 * 4 * np.linalg.det(transformation), "m^2")
```

**Output**
- (0,0) -> (0, 0)
- (6,0) -> (2.598, 1.5)
- (6,4) -> (1.598, 3.232)
- (0,4) -> (-1.0, 1.732)
- Determinant = 0.25; map area = 6 m^2

**Interpretation:** the room is drawn at half its linear size and turned 30 degrees. The determinant of 0.25 (0.5 x 0.5) shows that area shrinks to a quarter: 24 m^2 becomes 6 m^2 on the map. The room keeps its shape, because uniform scaling and rotation do not distort angles.

---
# TASK 6: Solution of Systems of Linear Equations
File: `code/Task_06_linear_systems.py`

## B. Input values and mathematical operation
**Inputs**
- Coefficient matrix A = [[4, 2],[8, 12]]. Row 1 is CPU use (4 per Type A, 2 per Type B). Row 2 is memory in GB (8 per Type A, 12 per Type B).
- Result vector b = [20, 72], the total CPU and total memory observed.
- Unknowns x = number of Type A servers, y = number of Type B servers.

**Operations**
1. Write the system as Ax = b:
   - 4x + 2y = 20
   - 8x + 12y = 72
2. Solve with `np.linalg.solve(A, b)`
3. Verify with `A @ solution`
4. Compute residual = b - A @ solution, and its norm

**Output:** Type A = 3, Type B = 4. A @ solution = [20, 72]. Residual = [0, 0] (or about 1e-15), and the residual norm is about 0.

## C. Change a parameter and explain
| Change | Result |
|---|---|
| b = [24, 80] (more CPU and memory) | Type A = 4, Type B = 4 |
| b = [20, 76] (memory changed only) | Type A = 2.75, Type B = 4.5 |

Explanation: larger totals mean more servers are active. With 76 GB the answer has a fraction (2.75), which is not a valid count of servers. The equations are solved correctly, but the data do not match a whole-number situation. The mathematical solution must always be checked against what makes sense in the real problem.

## D. Meaning of the output
The only combination of servers that uses exactly 20 CPU units and 72 GB of memory is 3 Type A servers and 4 Type B servers. Check: CPU = 4(3) + 2(4) = 20 and memory = 8(3) + 12(4) = 72. The determinant of A is 4(12) - 2(8) = 32, which is not zero, so the system has exactly one solution. The residual of zero confirms the answer satisfies both equations. If one row of A were a multiple of the other (determinant 0), there would be no single unique answer.

## E. Modified program: a different real-world case
**Case:** a farmer mixes two fertilizers. Fertilizer X is 20% nitrogen and 10% phosphorus. Fertilizer Y is 10% nitrogen and 30% phosphorus. The field needs exactly 50 kg of nitrogen and 60 kg of phosphorus. How many kg of each should be used?

**Assumptions**
- Only nitrogen and phosphorus matter.
- The percentages are exact and fixed.
- Amounts can be any real number of kg.
- The two nutrients are the only constraints.

**Equations**
- 0.20x + 0.10y = 50 (nitrogen)
- 0.10x + 0.30y = 60 (phosphorus)

```python
import numpy as np

# x = kg of Fertilizer X, y = kg of Fertilizer Y
A = np.array([[0.20, 0.10],    # nitrogen fraction in X and Y
              [0.10, 0.30]])   # phosphorus fraction in X and Y
b = np.array([50.0, 60.0])     # required kg of nitrogen and phosphorus

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Fertilizer X: {solution[0]:.1f} kg")
print(f"Fertilizer Y: {solution[1]:.1f} kg")
print("Nutrients supplied (N, P):", A @ solution)
print("Residual norm:", np.linalg.norm(residual))
print("Determinant:", np.linalg.det(A))
```

**Output**
- Fertilizer X: 180.0 kg
- Fertilizer Y: 140.0 kg
- Nutrients supplied: [50, 60]
- Residual norm: 0.0
- Determinant: 0.05

**Interpretation:** 180 kg of X and 140 kg of Y supply exactly 50 kg of nitrogen (36 + 14) and 60 kg of phosphorus (18 + 42). The determinant is non-zero, so this is the only mix that works. The zero residual confirms it.

---
## Submission reminder
- Each student submits their own GitHub repository (no group repos).
- Add the two files `Task_05_matrix_algebra.py` and `Task_06_linear_systems.py`, plus the new-case versions, and put this documentation in your README.
- Upload the GitHub link and documentation through VLMS.
