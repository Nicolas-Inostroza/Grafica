from .trasformaciones import mat_translate, mat_rotate_x, mat_rotate_y, mat_rotate_z, mat_mul, mat_identity
import math

Poses = {


    #Pose baspersonaje recto
    "neutral": {
        "torso_sup": {"translate": (0, 0, 0), "rotate_x": 0, "rotate_y": 0},
        "Torso_Central": {"rotate_x": 0, "rotate_y": 0},
        "Cadera": {"rotate_x": 0, "rotate_y": 0},
        "Cabeza": {"rotate_x": 0, "rotate_y": 0},
        "Brazo_Izq": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Brazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Antebrazo_Izq": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Antebrazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Pierna_Izq": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Pierna_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Pantorrilla_Izq": {"rotate_x": 0, "rotate_y": 0},
        "Pantorrilla_Der": {"rotate_x": 0, "rotate_y": 0},
    },
    
    # Pose de Johnny Joestar
    "johnny_joestar": {
        "torso_sup": {"translate": (0, 0, 0), "rotate_x": math.radians(10), "rotate_y": math.radians(-10)},
        "Torso_Central": {"rotate_x": math.radians(10), "rotate_y": math.radians(-35)},
        "Cadera": {"rotate_x": math.radians(20), "rotate_y": math.radians(10)},
        "Cabeza": {"rotate_x": math.radians(-5), "rotate_y": math.radians(-20)},
        
        # Brazo derecho apuntando hacia adelante (pose de disparo)
        "Brazo_Der": {"rotate_x": math.radians(40), "rotate_y": math.radians(30), "rotate_z": math.radians(-50)},
        "Antebrazo_Der": {"rotate_x": math.radians(110), "rotate_y": math.radians(50), "rotate_z": math.radians(0)},
        
        # Brazo izquierdo hacia atrás en ángulo dramático
        "Brazo_Izq": {"rotate_x": math.radians(30), "rotate_y": math.radians(0), "rotate_z": math.radians(25)},
        "Antebrazo_Izq": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": 0},
        
        # Piernas en posición estable
        "Pierna_Der": {"rotate_x": math.radians(20), "rotate_y": math.radians(-40), "rotate_z": math.radians(-10)},
        "Pierna_Izq": {"rotate_x": math.radians(10), "rotate_y": math.radians(0), "rotate_z":  math.radians(60)},
        "Pantorrilla_Der": {"rotate_x": math.radians(-100), "rotate_y": math.radians(90),"rotate_z": math.radians(0)},
        "Pantorrilla_Izq": {"rotate_x": math.radians(-150), "rotate_y": math.radians(40)},
        "Pie_Der": {"rotate_x": math.radians(0), "rotate_y": math.radians(-40), "rotate_z": 0},
        "Pie_Izq": {"rotate_x": math.radians(-70), "rotate_y": math.radians(-60), "rotate_z": math.radians(-30)},
    },
    
    # Pose imposible de Polnareff
    "polnareff_pose": {
        "torso_sup": {"rotate_x": math.radians(50), "rotate_y": math.radians(10),"rotate_z": math.radians(-20)},
        "Torso_Central": {"rotate_x": math.radians(20), "rotate_y": math.radians(-30),"rotate_z": math.radians(100)},
        "Cadera": {"rotate_x": math.radians(20), "rotate_y": math.radians(-30)},
        "Cabeza": {"rotate_x": math.radians(20), "rotate_y": 0,"rotate_z": math.radians(-10)},
        
        # Brazo derecho señalando
        "Brazo_Der": {"rotate_x": math.radians(150),"rotate_y": math.radians(0), "rotate_z": math.radians(40)},
        "Antebrazo_Der": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": math.radians(20)},
        
        # Brazo izquierdo en la cadera/cinturón
        "Brazo_Izq": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": math.radians(20)},
        "Antebrazo_Izq": {"rotate_x": math.radians(40), "rotate_y": math.radians(0), "rotate_z": 0},
        
        # Piernas en postura confiada
        "Pierna_Der": {"rotate_x": math.radians(-60), "rotate_y": math.radians(70), "rotate_z": 0},
        "Pierna_Izq": {"rotate_x": math.radians(100), "rotate_y": math.radians(40), "rotate_z": 0},
        "Pantorrilla_Der": {"rotate_x": math.radians(0), "rotate_y": 0},
        "Pantorrilla_Izq": {"rotate_x": math.radians(-50), "rotate_y": math.radians(30)},
        "Pie_Der": {"rotate_x": math.radians(-30), "rotate_y": math.radians(20), "rotate_z": 0},
        "Pie_Izq": {"rotate_x": math.radians(-40), "rotate_y": math.radians(10), "rotate_z": 0},
    },
    
    # Pose de Jonathan Joestar 
    "jonathan_pose": {
        "torso_sup": {"rotate_x": math.radians(0), "rotate_y": math.radians(-5),"rotate_z": math.radians(5)},
        "Torso_Central": {"rotate_x": math.radians(0), "rotate_y": math.radians(0),"rotate_z": math.radians(10)},
        "Cadera": {"rotate_x": 0, "rotate_y": math.radians(0),"rotate_z":math.radians(-10)},
        "Cabeza": {"rotate_x": math.radians(-10), "rotate_y": math.radians(0),"rotate_z":math.radians(10)},
        
        # Brazo derecho apuntando dramáticamente
        "Brazo_Der": {"rotate_x": math.radians(40), "rotate_y": math.radians(0), "rotate_z": math.radians(30)},
        "Antebrazo_Der": {"rotate_x": math.radians(20), "rotate_y": math.radians(0), "rotate_z":math.radians(130)},
        
        # Brazo izquierdo en ángulo hacia abajo
        "Brazo_Izq": {"rotate_x": math.radians(-20), "rotate_y": math.radians(0), "rotate_z": math.radians(20)},
        "Antebrazo_Izq": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": 0},
        
        # Piernas dinámicas
        "Pierna_Der": {"rotate_x": math.radians(25), "rotate_y": math.radians(0), "rotate_z": math.radians(-30)},
        "Pierna_Izq": {"rotate_x": math.radians(25), "rotate_y": math.radians(20), "rotate_z": math.radians(30)},
        "Pantorrilla_Der": {"rotate_x": math.radians(-25), "rotate_y": 0},
        "Pantorrilla_Izq": {"rotate_x": math.radians(-25), "rotate_y": 0},
        "Pie_Der": {"rotate_x": math.radians(-30), "rotate_y": math.radians(20), "rotate_z": 0},
        "Pie_Izq": {"rotate_x": math.radians(-40), "rotate_y": math.radians(-60), "rotate_z": 0},
    },
}


"""
aplicar_pose :: dict, string -> void
Aplica una pose especifica al personaje.
Busca una llave dentro del diccionario esto devuelve una lista de diccionarios cda uno contiene el nombre de un nodo del personaje
y las trasformaciones a aplicar para cada nodo.

"""
def aplicar_pose(personaje_dict, pose_nombre):
    
    pose = Poses[pose_nombre]
    
    # Devolvemos a todos los nodos a su posicion base
    for nodo_nombre, nodo in personaje_dict.items():
        nodo.set_transformacion(nodo.transformacion_local)
    
    # Para cada cosa del diccionario se obtiene el nombre del nodo y las transformadas a aplicar a este.
    for nodo_nombre, transforms in pose.items():

        # Nos aseguramos que el nodo al cual se le va a aplicar al transformacion existe en el personaje.
        if nodo_nombre in personaje_dict:
            nodo = personaje_dict[nodo_nombre]
            
            # La translación solo se aplica al nodo raíz es decir solo al Torso central cualquier otro intento de translación sera ignorado

            if nodo_nombre == "Torso_Central" and "translate" in transforms:
                tx, ty, tz = transforms["translate"]
                if tx != 0 or ty != 0 or tz != 0:
                    # Replace the local transformation with new translation
                    transform = mat_translate(tx, ty, tz)
            else:
                transform = nodo.transformacion_local
            
            # Se aplican las rotaciones en cada eje, al aplicarse una despues de otra cada rotacion es relativa a la anterior.
            if "rotate_x" in transforms and transforms["rotate_x"] != 0:
                transform = mat_mul(transform, mat_rotate_x(transforms["rotate_x"]))
            if "rotate_y" in transforms and transforms["rotate_y"] != 0:
                transform = mat_mul(transform, mat_rotate_y(transforms["rotate_y"]))
            if "rotate_z" in transforms and transforms["rotate_z"] != 0:
                transform = mat_mul(transform, mat_rotate_z(transforms["rotate_z"]))
            
            # Aplicamos la transformación resultante al nodo.
            nodo.set_transformacion(transform)