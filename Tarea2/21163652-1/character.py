"""
character.py - Define la estructura del personaje articulado
"""
from .scenegraph import SceneNode
from .geometry import create_cube, create_cylinder, create_sphere
from .transforms import translate, scale, rotate_x, rotate_y, rotate_z, matmul

def create_character():
    """
    Crea un personaje articulado con jerarquía
    Estructura: torso -> cabeza, brazo_izq, brazo_der, pierna_izq, pierna_der
    """
    
    # Nodo raíz (torso)
    torso = SceneNode("torso", create_cube(color=(0.8, 0.3, 0.3)))
    torso.set_transform(matmul(
        translate(0.1, 0.1, 0.1),
        scale(1, 1, 1)
    ))
   
    
    return torso