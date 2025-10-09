
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


def create_cylinder(radius=0.2, height=2.0, slices=32, axis='z'):
    vertices = []
    indices = []
    half = height / 2.0

    # --- Base cylinder vertices ---
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        c = radius * math.cos(angle)
        s = radius * math.sin(angle)

        if axis == 'y':
            v1 = [c, -half, s]  # base inferior
            v2 = [c,  half, s]  # base superior
        elif axis == 'x':
            v1 = [-half, c, s]
            v2 = [ half, c, s]
        else:  # 'z'
            v1 = [c, s, -half]
            v2 = [c, s,  half]

        vertices += v1 + v2

    # --- Build lateral indices ---
    for i in range(0, slices * 2, 2):
        indices += [
            i, i + 1, (i + 2) % (2 * (slices + 1)),
            i + 1, (i + 3) % (2 * (slices + 1)), (i + 2) % (2 * (slices + 1))
        ]

    # --- Add top and bottom center vertices ---
    if axis == 'y':
        bottom_center = [0, -half, 0]
        top_center = [0, half, 0]
    elif axis == 'x':
        bottom_center = [-half, 0, 0]
        top_center = [half, 0, 0]
    else:  # 'z'
        bottom_center = [0, 0, -half]
        top_center = [0, 0, half]

    bottom_center_index = len(vertices) // 3
    vertices += bottom_center
    top_center_index = len(vertices) // 3
    vertices += top_center

    # --- Add indices for bottom and top caps ---
    for i in range(slices):
        # Base inferior
        base_i = 2 * i
        next_i = (2 * (i + 1)) % (2 * (slices + 1))
        indices += [bottom_center_index, next_i, base_i]

        # Base superior
        top_i = 2 * i + 1
        next_top_i = (2 * (i + 1) + 1) % (2 * (slices + 1))
        indices += [top_center_index, top_i, next_top_i]


    return vertices, indices





def create_cube(size=1.0, scale_x=1.0, scale_y=1.0, scale_z=1.0):
    sx = (size * scale_x) / 2.0
    sy = (size * scale_y) / 2.0
    sz = (size * scale_z) / 2.0

    vertices = [
        # Cara frontal 
        -sx, -sy,  sz,   sx, -sy,  sz,   sx,  sy,  sz,  -sx,  sy,  sz,
        # Cara trasera
        -sx, -sy, -sz,  -sx,  sy, -sz,   sx,  sy, -sz,   sx, -sy, -sz,
        # Cara superior
        -sx,  sy, -sz,  -sx,  sy,  sz,   sx,  sy,  sz,   sx,  sy, -sz,
        # Cara inferior
        -sx, -sy, -sz,   sx, -sy, -sz,   sx, -sy,  sz,  -sx, -sy,  sz,
        # Cara derecha
         sx, -sy, -sz,   sx,  sy, -sz,   sx,  sy,  sz,   sx, -sy,  sz,
        # Cara izquierda
        -sx, -sy, -sz,  -sx, -sy,  sz,  -sx,  sy,  sz,  -sx,  sy, -sz,
    ]

    indices = [
        0,  1,  2,   0,  2,  3,   
        4,  5,  6,   4,  6,  7,   
        8,  9, 10,   8, 10, 11,   
        12, 13, 14,  12, 14, 15,  
        16, 17, 18,  16, 18, 19,  
        20, 21, 22,  20, 22, 23   
    ]

    return vertices, indices
