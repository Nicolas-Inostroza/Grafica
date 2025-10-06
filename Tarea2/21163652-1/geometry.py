"""
geometry.py - Definiciones de geometrías básicas (cubos, cilindros, esferas)
"""
import numpy as np
import math

def create_cube(color=(0, 1.0, 0.0)):
    """Crea un cubo centrado en el origen"""
    vertices = np.array([
        # Cara frontal
        -0.5, -0.5,  0.5,  *color,
         0.5, -0.5,  0.5,  *color,
         0.5,  0.5,  0.5,  *color,
        -0.5,  0.5,  0.5,  *color,
        # Cara trasera
        -0.5, -0.5, -0.5,  *color,
         0.5, -0.5, -0.5,  *color,
         0.5,  0.5, -0.5,  *color,
        -0.5,  0.5, -0.5,  *color,
    ], dtype=np.float32)
    
    indices = np.array([
        0, 1, 2, 2, 3, 0,  # Frontal
        4, 7, 6, 6, 5, 4,  # Trasera
        0, 4, 5, 5, 1, 0,  # Inferior
        2, 6, 7, 7, 3, 2,  # Superior
        0, 3, 7, 7, 4, 0,  # Izquierda
        1, 5, 6, 6, 2, 1,  # Derecha
    ], dtype=np.uint32)
    
    return vertices, indices

def create_cylinder(color=(0.0, 1.0, 0.0), segments=16):
    """Crea un cilindro orientado en el eje Y"""
    vertices = []
    indices = []
    
    # Crear círculos superior e inferior
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = 0.5 * math.cos(angle)
        z = 0.5 * math.sin(angle)
        
        # Vértice inferior
        vertices.extend([x, -0.5, z, *color])
        # Vértice superior
        vertices.extend([x, 0.5, z, *color])
    
    # Tapas
    vertices.extend([0.0, -0.5, 0.0, *color])  # Centro inferior
    vertices.extend([0.0, 0.5, 0.0, *color])   # Centro superior
    
    center_bottom = segments * 2
    center_top = segments * 2 + 1
    
    # Índices para las caras laterales
    for i in range(segments):
        next_i = (i + 1) % segments
        
        # Cara lateral (dos triángulos)
        indices.extend([
            i * 2, next_i * 2, i * 2 + 1,
            next_i * 2, next_i * 2 + 1, i * 2 + 1
        ])
        
        # Tapa inferior
        indices.extend([center_bottom, next_i * 2, i * 2])
        
        # Tapa superior
        indices.extend([center_top, i * 2 + 1, next_i * 2 + 1])
    
    return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)

def create_sphere(color=(0.0, 0.0, 1.0), stacks=10, slices=10):
    """Crea una esfera"""
    vertices = []
    indices = []
    
    for i in range(stacks + 1):
        phi = math.pi * i / stacks
        for j in range(slices + 1):
            theta = 2 * math.pi * j / slices
            
            x = 0.5 * math.sin(phi) * math.cos(theta)
            y = 0.5 * math.cos(phi)
            z = 0.5 * math.sin(phi) * math.sin(theta)
            
            vertices.extend([x, y, z, *color])
    
    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1
            
            indices.extend([first, second, first + 1])
            indices.extend([second, second + 1, first + 1])
    
    return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)