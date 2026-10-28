# BIT 2118 Scientific Computing: Tasks 5 and 6

**Name:** Joshua Lema Samuria

## Repository contents

| File | Description |
|---|---|
| `code/Task_05_matrix_algebra.py` | Task 5 original program |
| `code/Task_05_modified_room_map.py` | Task 5 modified program (room map) |
| `code/Task_06_linear_systems.py` | Task 6 original program |
| `code/Task_06_modified_fertilizer_mix.py` | Task 6 modified program (fertilizer mix) |
| `requirements.txt` | Python library needed (NumPy) |

## How to run

```
pip install -r requirements.txt
python code/Task_05_matrix_algebra.py
```

---

## Task 5: Matrix Algebra and Matrix Operations

### Inputs and operations
- Inputs: the four corners of a unit square, a 45 degree angle, and scale factors 2 (x) and 1.5 (y).
- Operations: build a rotation matrix R and a scaling matrix S, combine them as T = R @ S, transform every point with `points @ T.T`, and compute the determinant.

### Output
| Original | Transformed |
|---|---|
| (0, 0) | (0, 0) |
| (1, 0) | (1.414, 1.414) |
| (1, 1) | (0.354, 2.475) |
| (0, 1) | (-1.061, 1.061) |

Determinant = 3.0

### Changing a parameter
- Angle 45 to 90 degrees: the shape turns to a new orientation, but the determinant stays 3.0.
- Scale (2, 1.5) to (3, 1.5): the determinant becomes 4.5, so the area grows more.
- The angle changes direction only. The scale factors change size. Determinant = sx x sy.

### Meaning of the output
The unit square is stretched and rotated into a tilted parallelogram. The determinant of 3 means the area is three times larger (2 x 1.5). It is positive, so the shape is not mirrored. The origin stays fixed.

### Modified case: room map
- Case: a 6 m x 4 m room rotated 30 degrees and drawn at half size on a floor-plan map.
- Assumptions: origin at the bottom-left corner of the room, units in metres, uniform scale of 0.5, anticlockwise rotation.
- Input data: corners (0,0), (6,0), (6,4), (0,4); angle 30 degrees; scale (0.5, 0.5).
- Output: (0,0) to (0,0); (6,0) to (2.598, 1.5); (6,4) to (1.598, 3.232); (0,4) to (-1.0, 1.732). Determinant = 0.25.
- Interpretation: the room is drawn at half its linear size and turned 30 degrees. The area shrinks to a quarter (24 m^2 becomes 6 m^2). The rectangle keeps its shape because uniform scaling and rotation do not distort angles.

---

## Task 6: Solution of Systems of Linear Equations

### Inputs and operations
- Inputs: coefficient matrix A = [[4, 2], [8, 12]] (CPU and memory per server type) and totals b = [20, 72].
- Equations: 4x + 2y = 20 (CPU) and 8x + 12y = 72 (memory), where x = Type A servers and y = Type B servers.
- Operations: solve with `np.linalg.solve(A, b)`, verify with `A @ solution`, and compute the residual.

### Output
Type A = 3 servers, Type B = 4 servers. Residual is about 0.

### Changing a parameter
- Totals b = [24, 80]: Type A = 4, Type B = 4. More resources means more servers.
- Memory changed to 76: Type A = 2.75, Type B = 4.5. The fractions are not valid server counts, so the data does not fit a whole-number situation.

### Meaning of the output
The only combination that uses exactly 20 CPU units and 72 GB of memory is 3 Type A and 4 Type B servers. Check: CPU = 4(3) + 2(4) = 20 and memory = 8(3) + 12(4) = 72. The determinant of A is 32 (not zero), so the solution is unique. A residual of zero confirms the answer satisfies both equations.

### Modified case: fertilizer mix
- Case: a farmer mixes two fertilizers. X is 20% nitrogen and 10% phosphorus. Y is 10% nitrogen and 30% phosphorus. The field needs 50 kg of nitrogen and 60 kg of phosphorus.
- Assumptions: only nitrogen and phosphorus matter, percentages are exact, amounts can be any real number of kg.
- Equations: 0.20x + 0.10y = 50 and 0.10x + 0.30y = 60.
- Output: Fertilizer X = 180 kg, Fertilizer Y = 140 kg. Nutrients supplied = [50, 60]. Determinant = 0.05.
- Interpretation: 180 kg of X and 140 kg of Y supply exactly 50 kg of nitrogen (36 + 14) and 60 kg of phosphorus (18 + 42). The determinant is non-zero, so this is the only mix that works.
