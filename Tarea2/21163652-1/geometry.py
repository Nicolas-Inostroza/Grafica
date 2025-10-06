"""
geometry.py - Definiciones de geometrías básicas (cubos, cilindros, esferas)
"""
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
    """
    Crea un cilindro alineado con el eje especificado.
    axis: 'x', 'y', o 'z' (por defecto 'z' que es vertical)
    """
    vertices = []
    indices = []
    half = height / 2.0
    
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        c = radius * math.cos(angle)
        s = radius * math.sin(angle)
        
        if axis == 'y':  # Cilindro vertical (para brazos/piernas)
            vertices += [c, -half, s]
            vertices += [c,  half, s]
        elif axis == 'x':  # Cilindro horizontal en X
            vertices += [-half, c, s]
            vertices += [ half, c, s]
        else:  # axis == 'z' (default)
            vertices += [c, s, -half]
            vertices += [c, s,  half]
    
    for i in range(0, slices * 2, 2):
        indices += [
            i, i+1, (i+2) % (2*(slices+1)),
            i+1, (i+3) % (2*(slices+1)), (i+2) % (2*(slices+1))
        ]
    return vertices, indices

def create_cube(size=1.0):
    """Crea un cubo centrado en el origen"""
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