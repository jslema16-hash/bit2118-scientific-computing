import numpy as np

# Modified case: rotate and scale a 6 m x 4 m room for a floor-plan map.
# Assumptions: origin at the bottom-left corner of the room, units in metres,
# uniform scale of 0.5, anticlockwise rotation of 30 degrees.

# Corners of the room, each row is [x, y] in metres
room = np.array([
    [0.0, 0.0],
    [6.0, 0.0],
    [6.0, 4.0],
    [0.0, 4.0]
])

angle = np.deg2rad(30)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

scale = np.array([
    [0.5, 0.0],
    [0.0, 0.5]
])

transformation = rotation @ scale
map_points = room @ transformation.T

print("Room corners on the map:\n", np.round(map_points, 3))
print("Determinant:", np.linalg.det(transformation))
print("Original area:", 6 * 4, "m^2")
print("Map area:", 6 * 4 * np.linalg.det(transformation), "m^2")
