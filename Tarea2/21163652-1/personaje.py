

from .geometry import *
from .nodo import Nodo
from .trasformaciones import *
import pyglet
from pyglet import gl


'''
crear_personaje(shader) -> (list, Nodo)
Crea un grafo de escena que contiene los nodos de las articulaciones del personaje.
Utiliza diferentes formas geometricas para las distintas partes del cuerpo.
'''
def crear_personaje(shader):
    # --- Crear geometrías para cada parte del personaje ---

    # Cabeza: esfera
    verts_sphere, inds_sphere = create_sphere(radius=0.5)
    vlist_sphere = shader.vertex_list_indexed(len(verts_sphere)//3, gl.GL_TRIANGLES, inds_sphere,
                                            position=(('f', 3), verts_sphere))
    # Torso: cubo
    verts_cube, inds_cube = create_cube(size=1.3)
    vlist_cube = shader.vertex_list_indexed(len(verts_cube)//3, gl.GL_TRIANGLES, inds_cube,
                                            position=(('f', 3), verts_cube))

    # Brazos: cilindros creados en el eje Y
    verts_arm, inds_arm = create_cylinder(radius=0.15, height=0.7, axis='y')
    vlist_arm = shader.vertex_list_indexed(len(verts_arm)//3, gl.GL_TRIANGLES, inds_arm,
                                        position=(('f', 3), verts_arm))

    # Antebrazos: cilindros creados en el eje Y y rotados en x
    verts_antebrazo, inds_antebrazo = create_cylinder(radius=0.15, height=0.6, axis='y')
    vlist_antebrazo = shader.vertex_list_indexed(len(verts_antebrazo)//3, gl.GL_TRIANGLES, inds_antebrazo,
                                        position=(('f', 3), verts_antebrazo))

    # Piernas: cilindros cilindros creados en el eje Y y rotados en el eje x 
    verts_leg, inds_leg = create_cylinder(radius=0.2, height=0.6, axis='y', rotation=(-10, 'x'))
    vlist_leg = shader.vertex_list_indexed(len(verts_leg)//3, gl.GL_TRIANGLES, inds_leg,
                                        position=(('f', 3), verts_leg))

    # Pies: cubos pequeños
    verts_foot, inds_foot = create_cube(size=0.4)
    vlist_foot = shader.vertex_list_indexed(len(verts_foot)//3, gl.GL_TRIANGLES, inds_foot,
                                            position=(('f', 3), verts_foot))

    # Pantorrilla: cilindros creados en el eje Y y rotados en el eje x
    verts_pantorrilla, inds_pantorrilla = create_cylinder(radius=0.2, height=0.6, axis='y', rotation=(20, 'x'))
    vlist_pantorrilla = shader.vertex_list_indexed(len(verts_pantorrilla)//3, gl.GL_TRIANGLES, inds_pantorrilla,
                                        position=(('f', 3), verts_pantorrilla))

    # --- NODOS PERSONAJE ---
    # 1. Torso (raíz) 
    torso = Nodo("Torso")
    torso.model = vlist_cube
    torso.shader = shader
    torso.color = (0.3, 0.5, 0.8)
    torso.transformacion_local = mat_identity()  # Posición local fija
    

    # 2. Cabeza 
    cabeza = Nodo("Cabeza")
    cabeza.model = vlist_sphere
    cabeza.shader = shader
    cabeza.color = (1.0, 0.8, 0.6)
    cabeza.transformacion_local = mat_translate(0, 1.3, 0)  # Posición fija arriba del torso
    torso.agregar_hijo(cabeza)

    # 3. Brazo Izquierdo
    brazo_izq = Nodo("Brazo_Izq")
    brazo_izq.model = vlist_arm
    brazo_izq.shader = shader
    brazo_izq.color = (0.9, 0.7, 0.5)
    # SOLO posición, la geometría ya está orientada correctamente
    brazo_izq.transformacion_local = mat_translate(-1.0, 0.5, 0)
    torso.agregar_hijo(brazo_izq)

    # 3. Antebrazo Izquierdo
    antebrazo_izq = Nodo("Antebrazo_Izq")
    antebrazo_izq.model = vlist_antebrazo
    antebrazo_izq.shader = shader
    antebrazo_izq.color = (0.9, 0.7, 0.5)
    # SOLO posición, la geometría ya está orientada correctamente
    antebrazo_izq.transformacion_local = mat_translate(0, -0.8, 0)
    brazo_izq.agregar_hijo(antebrazo_izq)


    # 4. Brazo Derecho
    brazo_der = Nodo("Brazo_Der")
    brazo_der.model = vlist_arm
    brazo_der.shader = shader
    brazo_der.color = (0.9, 0.7, 0.5)
    brazo_der.transformacion_local = mat_translate(1.0, 0.5, 0)
    torso.agregar_hijo(brazo_der)

    # 3. Antebrazo Izquierdo
    antebrazo_der = Nodo("Antebrazo_Der")
    antebrazo_der.model = vlist_antebrazo
    antebrazo_der.shader = shader
    antebrazo_der.color = (0.9, 0.7, 0.5)
    # SOLO posición, la geometría ya está orientada correctamente
    antebrazo_der.transformacion_local = mat_translate(0, -0.8, 0)
    brazo_der.agregar_hijo(antebrazo_der)

    # 5. Pierna Izquierda
    pierna_izq = Nodo("Pierna_Izq")
    pierna_izq.model = vlist_leg
    pierna_izq.shader = shader
    pierna_izq.color = (0.2, 0.3, 0.6)
    pierna_izq.transformacion_local = mat_translate(-0.4, -1.0, 0)
    torso.agregar_hijo(pierna_izq)

    
    # 6. Pantorrilla Izquierda
    pantorrilla_izq= Nodo("Pantorrilla_Izq")
    pantorrilla_izq.model = vlist_pantorrilla 
    pantorrilla_izq.shader = shader
    pantorrilla_izq.color = (0.2, 0.3, 0.6)
    pantorrilla_izq.transformacion_local = mat_translate(0, -0.6, 0)
    pierna_izq.agregar_hijo(pantorrilla_izq)

    # 7. Pie Izquierdo
    pie_izq = Nodo("Pie_Izq")
    pie_izq.model = vlist_foot
    pie_izq.shader = shader
    pie_izq.color = (0.1, 0.1, 0.1)
    pie_izq.transformacion_local = mat_translate(0, -0.4, 0.2)
    pantorrilla_izq.agregar_hijo(pie_izq)


    # 8. Pierna Derecha
    pierna_der = Nodo("Pierna_Der")
    pierna_der.model = vlist_leg
    pierna_der.shader = shader
    pierna_der.color = (0.2, 0.3, 0.6)
    pierna_der.transformacion_local = mat_translate(0.4, -1.0, 0)
    torso.agregar_hijo(pierna_der)

    # 9. Pantorrilla Derecha
    pantorrilla_der= Nodo("Pantorrilla_Der")
    pantorrilla_der.model = vlist_pantorrilla
    pantorrilla_der.shader = shader
    pantorrilla_der.color = (0.2, 0.3, 0.6)
    pantorrilla_der.transformacion_local = mat_translate(0, -0.6, 0)
    pierna_der.agregar_hijo(pantorrilla_der)

    # 10. Pie Derecho
    pie_der = Nodo("Pie_Der")
    pie_der.model = vlist_foot
    pie_der.shader = shader
    pie_der.color = (0.1, 0.1, 0.1)
    pie_der.transformacion_local = mat_translate(0, -0.4, 0.2)
    pantorrilla_der.agregar_hijo(pie_der)


    torso.set_transformacion(mat_identity())
    # At the end of crear_personaje function:
    personaje_dict = {
        "Torso": torso,
        "Cabeza": cabeza,
        "Brazo_Izq": brazo_izq,
        "Brazo_Der": brazo_der,
        "Antebrazo_Izq": antebrazo_izq,
        "Antebrazo_Der": antebrazo_der,
        "Pierna_Izq": pierna_izq,
        "Pierna_Der": pierna_der,
        "Pantorrilla_Izq": pantorrilla_izq,
        "Pantorrilla_Der": pantorrilla_der,
        "Pie_Izq": pie_izq,
        "Pie_Der": pie_der
    }

    personaje_list = list(personaje_dict.values())
    return personaje_dict, personaje_list, torso