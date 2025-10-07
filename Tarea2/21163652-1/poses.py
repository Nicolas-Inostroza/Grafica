from .trasformaciones import mat_translate, mat_rotate_x, mat_rotate_y, mat_rotate_z, mat_mul, mat_identity
import math

# Define poses with rotations (in radians) for each body part
Poses = {
    "neutral": {
        "Torso": {"translate": (0, 0, 0), "rotate_x": 0, "rotate_y": 0},
        "Cabeza": {"rotate_x": 0, "rotate_y": 0},
        "Brazo_Izq": {"rotate_x": 0, "rotate_y": 0},
        "Brazo_Der": {"rotate_x": 0, "rotate_y": 0},
        "Pierna_Izq": {"rotate_x": 0, "rotate_y": 0},
        "Pierna_Der": {"rotate_x": 0, "rotate_y": 0},

    },
    
    "t_pose": {
        "Torso": {"translate": (0, 0, 0), "rotate_x": 0, "rotate_y": 0},
        "Brazo_Izq": { "rotate_x": 0, "rotate_y": 0, "rotate_z": 0},
        "Brazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": math.radians(-20)},
        "Antebrazo_Der": {"rotate_x": math.radians(10), "rotate_y": 0, "rotate_z": math.radians(70)},  # Compensar la rotación del cilindro
    },
    
    "walking": {
        "Torso": {"translate": (0, 0, 0), "rotate_x": 0, "rotate_y": 0},
        "Brazo_Izq": {"rotate_x": 0, "rotate_y": 0, "rotate_z": math.radians(160)},
        "Brazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": math.radians(-50)},
        "Antebrazo_Der": {"rotate_x": 0, "rotate_y": math.radians(90), "rotate_z": 0},  # Compensar la rotación del cilindro
        "Antebrazo_Izq": {"rotate_x": math.radians(25), "rotate_y": 0},  # Compensar la rotación del cilindro
        "Antebrazo_Der": {"rotate_x": math.radians(25), "rotate_y": 0},  # Compensar la rotación del cilindro
    },
    
    "sitting": {
        "Torso": {"translate": (0, -0.5, 0), "rotate_x": math.radians(10), "rotate_y": 0},
        "Pierna_Izq": {"rotate_x": math.radians(90), "rotate_y": 0},
        "Pierna_Der": {"rotate_x": math.radians(90), "rotate_y": 0},
        "Pantorrilla_Izq": {"rotate_x": math.radians(-90), "rotate_y": 0},
        "Pantorrilla_Der": {"rotate_x": math.radians(-90), "rotate_y": 0},
    },
    
    "waving": {
        "Torso": {"translate": (0, 0, 0), "rotate_x": 0, "rotate_y": 0},
        "Brazo_Der": {"rotate_x": 0, "rotate_y": 0, "rotate_z": math.radians(-120)},
        "Antebrazo_Der": {"rotate_x": math.radians(-45), "rotate_y": 0},
    }
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
            
            # Start with the local transformation (position relative to parent)
            transform = nodo.transformacion_local
            
            # Apply rotations in order: X, Y, Z
            if "rotate_x" in transforms and transforms["rotate_x"] != 0:
                transform = mat_mul(mat_rotate_x(transforms["rotate_x"]), transform)
            if "rotate_y" in transforms and transforms["rotate_y"] != 0:
                transform = mat_mul(mat_rotate_y(transforms["rotate_y"]), transform)
            if "rotate_z" in transforms and transforms["rotate_z"] != 0:
                transform = mat_mul(mat_rotate_z(transforms["rotate_z"]),transform)

            # Apply translation if it's the torso (root node)
            if "translate" in transforms:
                tx, ty, tz = transforms["translate"]
                if tx != 0 or ty != 0 or tz != 0:
                    transform = mat_mul(mat_translate(tx, ty, tz), transform)
            
            nodo.set_transformacion(transform)