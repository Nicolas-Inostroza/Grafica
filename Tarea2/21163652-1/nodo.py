import pyglet
from pyglet import gl
from .trasformaciones import mat_identity, mat_mul

class Nodo:
    def __init__(self, nombre="Nodo", shader=None, model=None, color=(1.0, 1.0, 1.0)):
        self.nombre = nombre
        self.hijos = []
        self.transformacion = mat_identity()        # transformación actual (puede cambiar)
        self.transformacion_local = mat_identity()  # transformación local fija (posición relativa al padre)
        self.model = model                          # geometría (vertex list)
        self.color = color
        self.shader = shader                        # referencia al shader externo

    def agregar_hijo(self, nodo_hijo):
        """Agrega un nodo hijo a este nodo"""
        self.hijos.append(nodo_hijo)

    def set_transformacion(self, transformacion):
        """Establece la transformación actual del nodo"""
        self.transformacion = transformacion
        for hijo in self.hijos:
            hijo.set_transformacion(hijo.transformacion_local)
            

    def draw(self, parent_matrix=None):
        """Dibuja el nodo y sus hijos aplicando transformaciones jerárquicas."""
        if parent_matrix is None:
            model_matrix = self.transformacion
        else:
            model_matrix = mat_mul(parent_matrix, self.transformacion)

        if self.model and self.shader:
            self.shader["model"] = model_matrix
            self.shader["color"] = self.color
            self.model.draw(gl.GL_TRIANGLES)

        # Dibujar hijos con la matriz acumulada
        for hijo in self.hijos:
            hijo.draw(model_matrix)