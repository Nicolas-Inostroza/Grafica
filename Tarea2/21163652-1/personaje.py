

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
    #torso_superior: cubo
    verts_cube_superior, inds_cube_superior = create_cube(size=0.8, scale_x=1.8, scale_y=1, scale_z=0.8)
    vlist_cube_superior = shader.vertex_list_indexed(len(verts_cube_superior)//3, gl.GL_TRIANGLES, inds_cube_superior,
                                            position=(('f', 3), verts_cube_superior))
    # torso_central: cubo
    verts_cube_central, inds_cube_central = create_cube(size=0.6, scale_x=1.8, scale_y=1, scale_z=0.6)
    vlist_cube_central = shader.vertex_list_indexed(len(verts_cube_central)//3, gl.GL_TRIANGLES, inds_cube_central,
                                            position=(('f', 3), verts_cube_central))
    # torso_inferior: cubo
    verts_cube_inferior, inds_cube_inferior = create_cube(size=0.5, scale_x=1.8, scale_y=1, scale_z=0.6)
    vlist_cube_inferior = shader.vertex_list_indexed(len(verts_cube_inferior)//3, gl.GL_TRIANGLES, inds_cube_inferior,
                                            position=(('f', 3), verts_cube_inferior))


    # Brazos: cilindros creados en el eje Y
    verts_arm, inds_arm = create_cylinder(radius=0.15, height=1, axis='y')
    vlist_arm = shader.vertex_list_indexed(len(verts_arm)//3, gl.GL_TRIANGLES, inds_arm,
                                        position=(('f', 3), verts_arm))

    # Antebrazos: cilindros creados en el eje Y y rotados en x
    verts_antebrazo, inds_antebrazo = create_cylinder(radius=0.15, height=0.8, axis='y')
    vlist_antebrazo = shader.vertex_list_indexed(len(verts_antebrazo)//3, gl.GL_TRIANGLES, inds_antebrazo,
                                        position=(('f', 3), verts_antebrazo))

    verts_mano, inds_mano = create_sphere(radius=0.16, slices=20, stacks=10)
    vlist_mano = shader.vertex_list_indexed(len(verts_mano)//3, gl.GL_TRIANGLES, inds_mano,
                                            position=(('f', 3), verts_mano))

    verts_pelo, inds_pelo = create_cylinder(radius=0.45,height=0.8, slices=16, axis='y')
    vlist_pelo = shader.vertex_list_indexed(len(verts_pelo)//3, gl.GL_TRIANGLES, inds_pelo,
                                            position=(('f', 3), verts_pelo))



    # Piernas: cilindros cilindros creados en el eje Y y rotados en el eje x 
    verts_leg, inds_leg = create_cylinder(radius=0.2, height=0.9, axis='y',)
    vlist_leg = shader.vertex_list_indexed(len(verts_leg)//3, gl.GL_TRIANGLES, inds_leg,
                                        position=(('f', 3), verts_leg))

    # Pies: cubos pequeños
    verts_foot, inds_foot = create_cube(size=0.5, scale_x=0.5, scale_y=0.4, scale_z=1.5)
    vlist_foot = shader.vertex_list_indexed(len(verts_foot)//3, gl.GL_TRIANGLES, inds_foot,
                                            position=(('f', 3), verts_foot))

    # Pantorrilla: cilindros creados en el eje Y y rotados en el eje x
    verts_pantorrilla, inds_pantorrilla = create_cylinder(radius=0.2, height=0.8, axis='y')
    vlist_pantorrilla = shader.vertex_list_indexed(len(verts_pantorrilla)//3, gl.GL_TRIANGLES, inds_pantorrilla,
                                        position=(('f', 3), verts_pantorrilla))

    # --- NODOS PERSONAJE ---
    # 0. Crear nodos del personaje
    torso_central = Nodo("torso_central")  # Nodo central para mover todo el personaje
    torso_central.model = vlist_cube_central
    torso_central.shader = shader
    torso_central.color = (1.0, 1.0, 1.0)  # Color blanco por defecto
    torso_central.transformacion_local = mat_identity()  # Posición inicial en el origen

    # 1. torso_sup (raíz) 
    torso_sup = Nodo("torso_sup")
    torso_sup.model = vlist_cube_superior
    torso_sup.shader = shader
    torso_sup.color = (0.3, 0.5, 0.8)
    torso_sup.transformacion_local = mat_translate(0,0.8,0)  # Posición local fija
    torso_central.agregar_hijo(torso_sup)

    cadera = Nodo("Cadera")
    cadera.model = vlist_cube_inferior
    cadera.shader = shader
    cadera.color = (0.3, 0.5, 0.8)
    cadera.transformacion_local = mat_translate(0, -0.65, 0)  # Posición local fija
    torso_central.agregar_hijo(cadera)

    # 2. Cabeza 
    cabeza = Nodo("Cabeza")
    cabeza.model = vlist_sphere
    cabeza.shader = shader
    cabeza.color = (1.0, 0.8, 0.6)
    cabeza.transformacion_local = mat_translate(0, 1, 0)  # Posición fija arriba del torso_sup
    torso_sup.agregar_hijo(cabeza)

    # Pelo
    pelo = Nodo("Pelo")
    pelo.model = vlist_pelo
    pelo.shader = shader
    pelo.color = (1, 1, 1)
    pelo.transformacion_local = mat_translate(0, 0.6, 0)
    cabeza.agregar_hijo(pelo)







    # Hombro Izquierdo
    hombro_izq = Nodo("Hombro_Izq")
    hombro_izq.model = vlist_mano  # No tiene geometría propia
    hombro_izq.shader = shader
    hombro_izq.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    hombro_izq.transformacion_local = mat_translate(-0.9, 0.3, 0)
    torso_sup.agregar_hijo(hombro_izq)

    # 3. Brazo Izquierdo
    brazo_izq = Nodo("Brazo_Izq")
    brazo_izq.model = vlist_arm
    brazo_izq.shader = shader
    brazo_izq.color = (0.9, 0.7, 0.5)
    # SOLO posición, la geometría ya está orientada correctamente
    brazo_izq.transformacion_local = mat_translate(-0.05, -0.5, 0)
    hombro_izq.agregar_hijo(brazo_izq)


    # 4. Codo Izquierdo
    codo_izq = Nodo("Codo_Izq")
    codo_izq.model = vlist_mano  # No tiene geometría propia
    codo_izq.shader = shader
    codo_izq.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    codo_izq.transformacion_local = mat_translate(0, -0.6, 0)
    brazo_izq.agregar_hijo(codo_izq)

    # 3. Antebrazo Izquierdo
    antebrazo_izq = Nodo("Antebrazo_Izq")
    antebrazo_izq.model = vlist_antebrazo
    antebrazo_izq.shader = shader
    antebrazo_izq.color = (0.9, 0.7, 0.5)
    # SOLO posición, la geometría ya está orientada correctamente
    antebrazo_izq.transformacion_local = mat_translate(0, -0.5, 0)
    codo_izq.agregar_hijo(antebrazo_izq)

    #Mano Izquierda
    mano_izq = Nodo("Mano_Izq")
    mano_izq.model = vlist_mano  # Usamos la geometría del pie para
    mano_izq.shader = shader
    mano_izq.color = (1, 0.7, 0.7)
    mano_izq.transformacion_local = mat_translate(0, -0.6, 0)
    antebrazo_izq.agregar_hijo(mano_izq)







    # Hombro Derecho
    hombro_der = Nodo("Hombro_Der")
    hombro_der.model = vlist_mano  # No tiene geometría propia
    hombro_der.shader = shader
    hombro_der.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    hombro_der.transformacion_local = mat_translate(0.9, 0.3, 0)
    torso_sup.agregar_hijo(hombro_der)

    # 4. Brazo Derecho
    brazo_der = Nodo("Brazo_Der")
    brazo_der.model = vlist_arm
    brazo_der.shader = shader
    brazo_der.color = (0.9, 0.7, 0.5)
    brazo_der.transformacion_local = mat_translate(0.05, -0.5, 0)
    hombro_der.agregar_hijo(brazo_der)

    # 5. Codo Derecho
    codo_der = Nodo("Codo_Der")
    codo_der.model = vlist_mano  # No tiene geometría propia
    codo_der.shader = shader
    codo_der.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    codo_der.transformacion_local = mat_translate(0, -0.6, 0)
    brazo_der.agregar_hijo(codo_der)

    # 3. Antebrazo Izquierdo
    antebrazo_der = Nodo("Antebrazo_Der")
    antebrazo_der.model = vlist_antebrazo
    antebrazo_der.shader = shader
    antebrazo_der.color = (0.9, 0.7, 0.5)
    # SOLO posición, la geometría ya está orientada correctamente
    antebrazo_der.transformacion_local = mat_translate(0, -0.5, 0)
    codo_der.agregar_hijo(antebrazo_der)

    mano_der = Nodo("Mano_Der")
    mano_der.model = vlist_mano  # Usamos la geometría del pie para
    mano_der.shader = shader
    mano_der.color = (1, 0.7, 0.7)
    mano_der.transformacion_local = mat_translate(0, -0.6, 0)
    antebrazo_der.agregar_hijo(mano_der)







    # Union cadera - piernas Izquierda
    cad_pierna_izq = Nodo("Cad_Pierna_Izq")
    cad_pierna_izq.model = vlist_mano  # No tiene geometría propia
    cad_pierna_izq.shader = shader
    cad_pierna_izq.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    cad_pierna_izq.transformacion_local = mat_translate(-0.4, -0.3, 0)
    cadera.agregar_hijo(cad_pierna_izq)

    # 5. Pierna Izquierda
    pierna_izq = Nodo("Pierna_Izq")
    pierna_izq.model = vlist_leg
    pierna_izq.shader = shader
    pierna_izq.color = (0.2, 0.3, 0.6)
    pierna_izq.transformacion_local = mat_translate(0, -0.5, 0)
    cad_pierna_izq.agregar_hijo(pierna_izq)

    # Rodilla Izquierda
    rodilla_izq = Nodo("Rodilla_Izq")
    rodilla_izq.model = vlist_mano  # No tiene geometría propia
    rodilla_izq.shader = shader
    rodilla_izq.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    rodilla_izq.transformacion_local = mat_translate(0, -0.6, 0)
    pierna_izq.agregar_hijo(rodilla_izq)

    # 6. Pantorrilla Izquierda
    pantorrilla_izq= Nodo("Pantorrilla_Izq")
    pantorrilla_izq.model = vlist_pantorrilla 
    pantorrilla_izq.shader = shader
    pantorrilla_izq.color = (0.2, 0.3, 0.6)
    pantorrilla_izq.transformacion_local = mat_translate(0, -0.5, 0)
    rodilla_izq.agregar_hijo(pantorrilla_izq)

    #Conexión pie izquierdo
    conct_pie_izq = Nodo("Conct_Pie_Izq")
    conct_pie_izq.model = vlist_mano  # No tiene geometría propia
    conct_pie_izq.shader = shader
    conct_pie_izq.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    conct_pie_izq.transformacion_local = mat_translate(0, -0.4, 0)
    pantorrilla_izq.agregar_hijo(conct_pie_izq)

    # 7. Pie Izquierdo
    pie_izq = Nodo("Pie_Izq")
    pie_izq.model = vlist_foot
    pie_izq.shader = shader
    pie_izq.color = (0.5, 0.5, 0.5)
    pie_izq.transformacion_local = mat_translate(0, -0.2, 0.2)
    conct_pie_izq.agregar_hijo(pie_izq)









    # Union cadera - piernas Derecha
    cad_pierna_der = Nodo("Cad_Pierna_Der")
    cad_pierna_der.model = vlist_mano  # No tiene geometría propia
    cad_pierna_der.shader = shader
    cad_pierna_der.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    cad_pierna_der.transformacion_local = mat_translate(0.4, -0.3, 0)
    cadera.agregar_hijo(cad_pierna_der)

    # 8. Pierna Derecha
    pierna_der = Nodo("Pierna_Der")
    pierna_der.model = vlist_leg
    pierna_der.shader = shader
    pierna_der.color = (0.2, 0.3, 0.6)
    pierna_der.transformacion_local = mat_translate(0, -0.5, 0)
    cad_pierna_der.agregar_hijo(pierna_der)

    # Rodilla Derecha
    rodilla_der = Nodo("Rodilla_Der")
    rodilla_der.model = vlist_mano  # No tiene geometría propia
    rodilla_der.shader = shader
    rodilla_der.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    rodilla_der.transformacion_local = mat_translate(0, -0.6, 0)
    pierna_der.agregar_hijo(rodilla_der)

    # 9. Pantorrilla Derecha
    pantorrilla_der= Nodo("Pantorrilla_Der")
    pantorrilla_der.model = vlist_pantorrilla
    pantorrilla_der.shader = shader
    pantorrilla_der.color = (0.2, 0.3, 0.6)
    pantorrilla_der.transformacion_local = mat_translate(0, -0.5, 0)
    rodilla_der.agregar_hijo(pantorrilla_der)


    #Conexión pie derecho
    conct_pie_der = Nodo("Conct_Pie_Der")
    conct_pie_der.model = vlist_mano  # No tiene geometría propia
    conct_pie_der.shader = shader
    conct_pie_der.color = (1.0, 0.0, 0.0)  # Color rojo para identificar
    conct_pie_der.transformacion_local = mat_translate(0, -0.4, 0)
    pantorrilla_der.agregar_hijo(conct_pie_der)

    # 10. Pie Derecho
    pie_der = Nodo("Pie_Der")
    pie_der.model = vlist_foot
    pie_der.shader = shader
    pie_der.color = (0.5, 0.5, 0.5)
    pie_der.transformacion_local = mat_translate(0, -0.2, 0.2)
    conct_pie_der.agregar_hijo(pie_der)

    
    
    torso_central.set_transformacion(mat_identity())
    # At the end of crear_personaje function:
    personaje_dict = {
        "torso_sup": torso_sup,
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
        "Pie_Der": pie_der,
        "Cadera": cadera,
        "Torso_Central": torso_central,
        "Mano_Der": mano_der,
        "Codo_Der": codo_der,
        "Mano_Izq": mano_izq,
        "Codo_Izq": codo_izq,
        "Hombro_Der": hombro_der,
        "Hombro_Izq": hombro_izq,
        "Rodilla_Der": rodilla_der,
        "Rodilla_Izq": rodilla_izq,
        "Cad_Pierna_Der": cad_pierna_der,
        "Cad_Pierna_Izq": cad_pierna_izq,
        "Conct_Pie_Der": conct_pie_der,
        "Conct_Pie_Izq": conct_pie_izq,
        "Pelo": pelo,
    }

    personaje_list = list(personaje_dict.values())
    return personaje_dict, personaje_list, torso_central