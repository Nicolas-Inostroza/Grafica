
import numpy as np
import math

def create_sphere(radius=1.0, slices=32, stacks=16):
    vertices = []
    indices = []
    for i in range(stacks + 1):
        lat = math.pi * (-0.5 + float(i) / stacks)
        z = radius * math.sin(lat)
        r = radius * math.cos(lat)
        for j in range(slices + 1):
            lon = 2 * math.pi * float(j) / slices
            x = r * math.cos(lon)
            y = r * math.sin(lon)
            vertices += [x, y, z]
    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1
            indices += [first, second, first + 1,
                        second, second + 1, first + 1]
    return vertices, indices

def create_cylinder(radius=0.2, height=2.0, slices=32, axis='z', rotation=None):
    vertices = []
    indices = []
    half = height / 2.0
    
    # --- Base cylinder vertices ---
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        c = radius * math.cos(angle)
        s = radius * math.sin(angle)
        
        if axis == 'y':
            v1 = [c, -half, s]
            v2 = [c,  half, s]
        elif axis == 'x':
            v1 = [-half, c, s]
            v2 = [ half, c, s]
        else:  # 'z'
            v1 = [c, s, -half]
            v2 = [c, s,  half]
        
        vertices += v1 + v2
    
    # --- Apply rotation if needed ---
    if rotation is not None:
        angle_deg, rot_axis = rotation
        angle_rad = math.radians(angle_deg)
        
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # rotation matrices
        if rot_axis == 'x':
            R = [
                [1, 0, 0],
                [0, cos_a, -sin_a],
                [0, sin_a, cos_a]
            ]
        elif rot_axis == 'y':
            R = [
                [cos_a, 0, sin_a],
                [0, 1, 0],
                [-sin_a, 0, cos_a]
            ]
        elif rot_axis == 'z':
            R = [
                [cos_a, -sin_a, 0],
                [sin_a, cos_a, 0],
                [0, 0, 1]
            ]
        else:
            raise ValueError("rotation axis must be 'x', 'y', or 'z'")
        
        # Apply rotation to all vertices
        rotated_vertices = []
        for i in range(0, len(vertices), 3):
            x, y, z = vertices[i:i+3]
            rx = R[0][0]*x + R[0][1]*y + R[0][2]*z
            ry = R[1][0]*x + R[1][1]*y + R[1][2]*z
            rz = R[2][0]*x + R[2][1]*y + R[2][2]*z
            rotated_vertices += [rx, ry, rz]
        vertices = rotated_vertices

    # --- Build indices ---
    for i in range(0, slices * 2, 2):
        indices += [
            i, i+1, (i+2) % (2*(slices+1)),
            i+1, (i+3) % (2*(slices+1)), (i+2) % (2*(slices+1))
        ]

    return vertices, indices




def create_cube(size=1.0):
    s = size / 2.0
    vertices = [
        # Front face
        -s, -s,  s,   s, -s,  s,   s,  s,  s,  -s,  s,  s,
        # Back face
        -s, -s, -s,  -s,  s, -s,   s,  s, -s,   s, -s, -s,
        # Top face
        -s,  s, -s,  -s,  s,  s,   s,  s,  s,   s,  s, -s,
        # Bottom face
        -s, -s, -s,   s, -s, -s,   s, -s,  s,  -s, -s,  s,
        # Right face
         s, -s, -s,   s,  s, -s,   s,  s,  s,   s, -s,  s,
        # Left face
        -s, -s, -s,  -s, -s,  s,  -s,  s,  s,  -s,  s, -s,
    ]
    
    indices = [
        0,  1,  2,   0,  2,  3,   # front
        4,  5,  6,   4,  6,  7,   # back
        8,  9, 10,   8, 10, 11,   # top
        12, 13, 14,  12, 14, 15,  # bottom
        16, 17, 18,  16, 18, 19,  # right
        20, 21, 22,  20, 22, 23   # left
    ]
    
    return vertices, indices