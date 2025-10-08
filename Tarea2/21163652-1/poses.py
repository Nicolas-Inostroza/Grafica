from .trasformaciones import mat_translate, mat_rotate_x, mat_rotate_y, mat_rotate_z, mat_mul, mat_identity
import math

# Define poses with rotations (in radians) for each body part
Poses = {
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
    
    # Pose icónica de Johnny Joestar - pose de tiro con Tusk
    "johnny_joestar": {
        "torso_sup": {"translate": (0, 0, 0), "rotate_x": math.radians(10), "rotate_y": math.radians(-10)},
        "Torso_Central": {"rotate_x": math.radians(10), "rotate_y": math.radians(-30)},
        "Cadera": {"rotate_x": math.radians(20), "rotate_y": math.radians(10)},
        "Cabeza": {"rotate_x": math.radians(-5), "rotate_y": math.radians(-20)},
        
        # Brazo derecho apuntando hacia adelante (pose de disparo)
        "Brazo_Der": {"rotate_x": math.radians(40), "rotate_y": 0, "rotate_z": 0},
        "Antebrazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": math.radians(30)},
        
        # Brazo izquierdo hacia atrás en ángulo dramático
        "Brazo_Izq": {"rotate_x": math.radians(30), "rotate_y": math.radians(-20), "rotate_z": 0},
        "Antebrazo_Izq": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": 0},
        
        # Piernas en posición estable
        "Pierna_Der": {"rotate_x": math.radians(30), "rotate_y": math.radians(-40), "rotate_z": math.radians(-40)},
        "Pierna_Izq": {"rotate_x": math.radians(30), "rotate_y": math.radians(40), "rotate_z":  math.radians(40)},
        "Pantorrilla_Der": {"rotate_x": math.radians(-80), "rotate_y": math.radians(60)},
        "Pantorrilla_Izq": {"rotate_x": math.radians(-120), "rotate_y": math.radians(-60)},
    },
    
    # Pose de Jotaro - "Yare Yare Daze"
    "jotaro_pose": {
        "torso_sup": {"translate": (0, 0, 0), "rotate_x": math.radians(-10), "rotate_y": 0},
        "Torso_Central": {"rotate_x": math.radians(10), "rotate_y": math.radians(-80)},
        "Cadera": {"rotate_x": 0, "rotate_y": math.radians(10)},
        "Cabeza": {"rotate_x": math.radians(-20), "rotate_y": 0},
        
        # Brazo derecho señalando
        "Brazo_Der": {"rotate_x": math.radians(0), "rotate_y": math.radians(0), "rotate_z": math.radians(0)},
        "Antebrazo_Der": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": 0},
        
        # Brazo izquierdo en la cadera/cinturón
        "Brazo_Izq": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": math.radians(0)},
        "Antebrazo_Izq": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": 0},
        
        # Piernas en postura confiada
        "Pierna_Der": {"rotate_x": math.radians(10), "rotate_y": math.radians(-20), "rotate_z": 0},
        "Pierna_Izq": {"rotate_x": math.radians(-5), "rotate_y": math.radians(10), "rotate_z": 0},
        "Pantorrilla_Der": {"rotate_x": math.radians(-5), "rotate_y": 0},
        "Pantorrilla_Izq": {"rotate_x": math.radians(5), "rotate_y": 0},
    },
    
    # Pose de Joseph Joestar - "Your next line is..."
    "joseph_pose": {
        "torso_sup": {"translate": (0, 0, 0), "rotate_x": math.radians(0), "rotate_y": math.radians(-5),"rotate_z": math.radians(10)},
        "Torso_Central": {"rotate_x": math.radians(0), "rotate_y": math.radians(0)},
        "Cadera": {"rotate_x": 0, "rotate_y": math.radians(20)},
        "Cabeza": {"rotate_x": math.radians(-10), "rotate_y": math.radians(-30)},
        
        # Brazo derecho apuntando dramáticamente
        "Brazo_Der": {"rotate_x": math.radians(40), "rotate_y": math.radians(30), "rotate_z": math.radians(0)},
        "Antebrazo_Der": {"rotate_x": math.radians(0), "rotate_y": math.radians(0), "rotate_z":math.radians(40)},
        
        # Brazo izquierdo en ángulo hacia abajo
        "Brazo_Izq": {"rotate_x": math.radians(0), "rotate_y": math.radians(0), "rotate_z": math.radians(0)},
        "Antebrazo_Izq": {"rotate_x": math.radians(0), "rotate_y": 0, "rotate_z": 0},
        
        # Piernas dinámicas
        "Pierna_Der": {"rotate_x": math.radians(-10), "rotate_y": math.radians(-15), "rotate_z": 0},
        "Pierna_Izq": {"rotate_x": math.radians(25), "rotate_y": math.radians(20), "rotate_z": 0},
        "Pantorrilla_Der": {"rotate_x": math.radians(15), "rotate_y": 0},
        "Pantorrilla_Izq": {"rotate_x": math.radians(-15), "rotate_y": 0},
    },
    
    # Pose de Dio - "WRYYYY!"
    "dio_pose": {
        "torso_sup": {"translate": (0, 0.2, 0), "rotate_x": math.radians(-15), "rotate_y": 0},
        "Torso_Central": {"rotate_x": math.radians(-10), "rotate_y": 0},
        "Cadera": {"rotate_x": math.radians(5), "rotate_y": 0},
        "Cabeza": {"rotate_x": math.radians(-20), "rotate_y": 0},
        
        # Ambos brazos hacia arriba dramáticamente
        "Brazo_Der": {"rotate_x": math.radians(-140), "rotate_y": math.radians(-20), "rotate_z": math.radians(-40)},
        "Antebrazo_Der": {"rotate_x": math.radians(-30), "rotate_y": 0, "rotate_z": 0},
        
        "Brazo_Izq": {"rotate_x": math.radians(-140), "rotate_y": math.radians(20), "rotate_z": math.radians(40)},
        "Antebrazo_Izq": {"rotate_x": math.radians(-30), "rotate_y": 0, "rotate_z": 0},
        
        # Piernas en posición de poder
        "Pierna_Der": {"rotate_x": math.radians(-20), "rotate_y": math.radians(-15), "rotate_z": 0},
        "Pierna_Izq": {"rotate_x": math.radians(-20), "rotate_y": math.radians(15), "rotate_z": 0},
        "Pantorrilla_Der": {"rotate_x": math.radians(25), "rotate_y": 0},
        "Pantorrilla_Izq": {"rotate_x": math.radians(25), "rotate_y": 0},
    },
    
    # Pose de Giorno - "I, Giorno Giovanna, have a dream"
    "giorno_pose": {
        "torso_sup": {"translate": (0, 0, 0), "rotate_x": math.radians(5), "rotate_y": math.radians(-15)},
        "Torso_Central": {"rotate_x": math.radians(5), "rotate_y": math.radians(-10)},
        "Cadera": {"rotate_x": 0, "rotate_y": math.radians(-5)},
        "Cabeza": {"rotate_x": math.radians(-15), "rotate_y": math.radians(20)},
        
        # Mano derecha cerca del pecho (pose elegante)
        "Brazo_Der": {"rotate_x": math.radians(-50), "rotate_y": math.radians(-30), "rotate_z": math.radians(-70)},
        "Antebrazo_Der": {"rotate_x": math.radians(-60), "rotate_y": 0, "rotate_z": 0},
        
        # Brazo izquierdo extendido ligeramente
        "Brazo_Izq": {"rotate_x": math.radians(-30), "rotate_y": math.radians(20), "rotate_z": math.radians(50)},
        "Antebrazo_Izq": {"rotate_x": math.radians(-20), "rotate_y": 0, "rotate_z": 0},
        
        # Pose de piernas estilizada
        "Pierna_Der": {"rotate_x": math.radians(5), "rotate_y": math.radians(-10), "rotate_z": 0},
        "Pierna_Izq": {"rotate_x": math.radians(-5), "rotate_y": math.radians(15), "rotate_z": 0},
        "Pantorrilla_Der": {"rotate_x": math.radians(0), "rotate_y": 0},
        "Pantorrilla_Izq": {"rotate_x": math.radians(5), "rotate_y": 0},
    },
    
    # T-Pose básica
    "t_pose": {
        "torso_sup": {"translate": (0, 0, 0), "rotate_x": 0, "rotate_y": 0},
        "Brazo_Izq": {"rotate_x": 0, "rotate_y": 0, "rotate_z": math.radians(90)},
        "Brazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": math.radians(-90)},
        "Antebrazo_Izq": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Antebrazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
    },
}


def apply_pose(personaje_dict, pose_name):
    """
    Apply a pose to the character.
    
    Args:
        personaje_dict: Dictionary mapping node names to Nodo objects
        pose_name: Name of the pose from Poses dictionary
    """
    if pose_name not in Poses:
        print(f"Pose '{pose_name}' not found!")
        return
    
    pose = Poses[pose_name]
    
    # First, reset all nodes to their base local transformations
    for nodo_name, nodo in personaje_dict.items():
        nodo.set_transformacion(nodo.transformacion_local)
    
    # Then apply pose-specific transformations
    for nodo_name, transforms in pose.items():
        if nodo_name in personaje_dict:
            nodo = personaje_dict[nodo_name]
            
            # For root nodes: can modify translation (to move whole character)
            if nodo_name in ["torso_sup", "Torso_Central", "Cadera"] and "translate" in transforms:
                tx, ty, tz = transforms["translate"]
                if tx != 0 or ty != 0 or tz != 0:
                    # Replace the local transformation with new translation
                    transform = mat_translate(tx, ty, tz)
                else:
                    transform = nodo.transformacion_local
            else:
                # For ALL OTHER NODES: start with their fixed local transformation
                transform = nodo.transformacion_local
            
            # Apply rotations in order: X, Y, Z
            # Rotations are ALWAYS relative to the local position
            if "rotate_x" in transforms and transforms["rotate_x"] != 0:
                transform = mat_mul(transform, mat_rotate_x(transforms["rotate_x"]))
            if "rotate_y" in transforms and transforms["rotate_y"] != 0:
                transform = mat_mul(transform, mat_rotate_y(transforms["rotate_y"]))
            if "rotate_z" in transforms and transforms["rotate_z"] != 0:
                transform = mat_mul(transform, mat_rotate_z(transforms["rotate_z"]))
            
            nodo.set_transformacion(transform)