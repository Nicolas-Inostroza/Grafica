"""
poses.py - Define las poses dramáticas del personaje y sus configuraciones de cámara
"""
from .transforms import translate, rotate_x, rotate_y, rotate_z, matmul, look_at,perspective
from .character import create_character

class Pose:
    """Clase que encapsula una pose con su configuración de cámara"""
    
    def __init__(self, name, joint_rotations, camera_config):
        self.name = name
        self.joint_rotations = joint_rotations  # Dict: {node_name: (rx, ry, rz)}
        self.camera_config = camera_config  # (eye, center, up, fov)

# Definición de las 3 poses dramáticas

POSE_1_HERO = Pose(
    name="Pose Heroica",
    joint_rotations={
        "torso": (0, 0, 0),
        "head": (0, 0, 0),
        "left_shoulder": (0, 0, 0),
        "left_upper_arm": (0, 0, 0),
        "left_lower_arm": (0, 0, 0),
        "right_shoulder": (0, 0, 0),
        "right_upper_arm": (0, 0, 0),
        "right_lower_arm": (0, 0, 0),
        "left_hip": (0, 0, 0),
        "left_upper_leg": (0, 0, 0),
        "left_lower_leg": (0, 0, 0),
        "right_hip": (0, 0, 0),
        "right_upper_leg": (0, 0, 0),
        "right_lower_leg": (0, 0, 0),
    },
    camera_config=(
        [5, 2, 8],      # eye: más cerca y centrado
        [0, 0, 0],      # center: mirando al origen
        [0, 1, 0],      # up
        45              # fov: campo de visión normal
    )
)

POSE_2_DRAMATIC = Pose(
    name="Pose Dramática",
    joint_rotations={
        "torso": (0, -30, 10),
        "head": (-20, 30, 0),
        "left_shoulder": (0, 0, -90),
        "left_upper_arm": (0, 0, 0),
        "left_lower_arm": (-100, 0, 0),
        "right_shoulder": (0, 0, 90),
        "right_upper_arm": (0, 0, 0),
        "right_lower_arm": (-100, 0, 0),
        "left_hip": (0, 0, 0),
        "left_upper_leg": (0, 0, 0),
        "left_lower_leg": (0, 0, 0),
        "right_hip": (0, 0, 0),
        "right_upper_leg": (-60, 0, 0),
        "right_lower_leg": (90, 0, 0),
    },
    camera_config=(
        [6, -1, 5],     # eye: ángulo bajo lateral
        [0, 0.5, 0],    # center: mirando al personaje
        [0, 1, 0],      # up
        55              # fov: perspectiva ligeramente amplia
    )
)

POSE_3_VICTORY = Pose(
    name="Pose Victoria",
    joint_rotations={
        "torso": (10, 0, 0),
        "head": (20, 0, 0),
        "left_shoulder": (0, 0, -120),
        "left_upper_arm": (0, 0, 0),
        "left_lower_arm": (-150, 0, 0),
        "right_shoulder": (0, 0, 120),
        "right_upper_arm": (0, 0, 0),
        "right_lower_arm": (-150, 0, 0),
        "left_hip": (0, 0, 0),
        "left_upper_leg": (0, 0, 0),
        "left_lower_leg": (0, 0, 0),
        "right_hip": (0, 0, 0),
        "right_upper_leg": (0, 0, 0),
        "right_lower_leg": (0, 0, 0),
    },
    camera_config=(
        [4, 4, 6],      # eye: desde arriba diagonal
        [0, 0, 0],      # center: mirando al centro
        [0, 1, 0],      # up
        45              # fov: campo normal
    )
)

# Lista de todas las poses
POSES = [POSE_1_HERO, POSE_2_DRAMATIC, POSE_3_VICTORY]

def apply_pose(character_root, pose):
    """Aplica una pose al personaje modificando las transformaciones de sus nodos"""
    # Primero necesitamos obtener las transformaciones originales antes de aplicar rotaciones
    # Para esto, reconstruimos las transformaciones base de character.py

    
    # Crear un personaje temporal para obtener transformaciones base
    temp_character = create_character()
    
    for joint_name, rotations in pose.joint_rotations.items():
        node = character_root.find_node(joint_name)
        temp_node = temp_character.find_node(joint_name)
        
        if node and temp_node:
            rx, ry, rz = rotations
            
            # Obtener la transformación base original
            base_transform = temp_node.transform
            
            # Crear matriz de rotación
            rotation_transform = matmul(
                rotate_x(rx),
                rotate_y(ry),
                rotate_z(rz)
            )
            
            # Aplicar rotación después de la transformación base
            # La rotación se aplica en el espacio local del nodo
            new_transform = base_transform @ rotation_transform
            node.set_transform(new_transform)

def get_camera_matrices(pose, aspect_ratio):
    """Retorna las matrices de vista y proyección para una pose"""
    
    eye, center, up, fov = pose.camera_config
    
    view_matrix = look_at(eye, center, up)
    projection_matrix = perspective(fov, aspect_ratio, 0.1, 100.0)
    
    return view_matrix, projection_matrix