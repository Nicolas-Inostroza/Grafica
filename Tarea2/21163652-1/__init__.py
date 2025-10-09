import math
import pyglet
from pyglet import gl

from .geometry import create_sphere, create_cylinder, create_cube
from .trasformaciones import mat_identity, mat_translate, mat_rotate_y, mat_rotate_x, mat_mul
from .nodo import Nodo
from .camara import perspective, look_at
from .personaje import crear_personaje
from .poses import aplicar_pose, Poses


#============================================#
#=================CAMARA=====================#
#============================================#

Camara_por_pose={"neutral":{
    "Position": [0,0,6],
    "yaw": -90,
    "pitch": 0},

    "johnny_joestar":{
    "Position": [-0.22,-1.40,5.17],
    "yaw": -81,
    "pitch": 14},

    "polnareff_pose":{
    "Position": [2.89,0.10,-3.13],
    "yaw": 136,
    "pitch": -6},

    "jonathan_pose":{
    "Position": [0,-2.2,5],
    "yaw": -84,
    "pitch": 20},
    }

def aplicar_camara(camara_dic,pose):
    global camera_pos, yaw, pitch
    camara = camara_dic[pose]
    camera_pos= camara["Position"]
    yaw = camara["yaw"]
    pitch = camara["pitch"]


window = pyglet.window.Window(800, 600, "Personaje Articulado", resizable=True)
gl.glClearColor(0.5, 0.2, 0.5, 1)


#============================================#
#=================SHADER=====================#
#============================================#
vertex_source = """
#version 330 core
in vec3 position;
uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;
void main()
{
    gl_Position = projection * view * model * vec4(position, 1.0);
}
"""

fragment_source = """
#version 330 core
out vec4 FragColor;
uniform vec3 color;
void main()
{
    FragColor = vec4(color, 1.0);
}
"""

shader = pyglet.graphics.shader.ShaderProgram(
    pyglet.graphics.shader.Shader(vertex_source, "vertex"),
    pyglet.graphics.shader.Shader(fragment_source, "fragment"),
)

projection = perspective(math.radians(65), window.width / window.height, 0.1, 100.0)



# --- Controles ---
camera_pos = [0, 0, 6]
yaw, pitch = -90, 0
speed = 0.1
sensitivity = 2.0


#============================================#
#==================PISO======================#
#============================================#

verts_piso, inds_piso = create_cube(size=12, scale_x=1, scale_y=0.001, scale_z=1)
vlist_piso = shader.vertex_list_indexed(len(verts_piso)//3, gl.GL_TRIANGLES, inds_piso,
                                        position=(('f', 3), verts_piso))
piso = Nodo("Piso")
piso.model = vlist_piso
piso.shader = shader
piso.color = (0.1,0.1,0.1)
piso.transformacion= mat_translate(0, -3.5, 0)

piso_dic={"neutral":{
    "Posicion": [0,-3.5,0],},

    "johnny_joestar":{
    "Posicion": [0,-1.7,0],},

    "polnareff_pose":{
    "Posicion": [0,-1.3,0],},

    "jonathan_pose":{
    "Posicion": [0,-3.1,0],},
    }

def cambiar_piso(pose):
    if pose in piso_dic:
        posicion =piso_dic[pose]
        x,y,z = posicion["Posicion"]
        piso.transformacion=mat_translate(x,y,z)
#=================================================================================#
#=================================================================================#




#=================================================================================#
#=================================================================================#
# Valores para iniciales.
pos_torso = [0.0, 0.0, 0.0]  # Posición del torso
personaje_dict, cuerpo, torso = crear_personaje(shader)

# Lista de todas las poses disponibles
pose_list = list(Poses.keys())
pose_actual_index = 0
pose_actual = pose_list[pose_actual_index]
aplicar_pose(personaje_dict, pose_actual)  # Aplicar pose inicial

# Variable para evitar que la pose cambie si se mantiene el espacio
space_pressed = False

#==================================================================================#




def tarea():
    global pose_actual, pose_actual_index, space_pressed  # Agregar variables globales

    keys = pyglet.window.key.KeyStateHandler()
    window.push_handlers(keys)
    

    info_label = pyglet.text.Label(
        "",                             # Texto que se actualizara cada frame
        font_name="Arial",
        font_size=14,
        x=10, y=window.height - 20,     # Posicion del texto
        anchor_x="left", anchor_y="top",
        color=(255, 255, 255, 255) 
    )

    # Segun los valores de la camara que van cambiando actualizamos la vista
    def get_view():
        front = [
            math.cos(math.radians(yaw)) * math.cos(math.radians(pitch)),
            math.sin(math.radians(pitch)),
            math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
        ]
        target = [camera_pos[i] + front[i] for i in range(3)]
        return look_at(camera_pos, target, [0,1,0])

    @window.event
    def on_draw():
        window.clear()
        gl.glEnable(gl.GL_DEPTH_TEST)
        shader.use()
        shader["projection"] = projection
        shader["view"] = get_view()

        # Dibujar todo el árbol
        torso.draw(None)
        piso.draw(None)
        


        gl.glDisable(gl.GL_DEPTH_TEST)
        # Para que se actualizen los valores de la camara en pantalla
        info_label.text = f"Pos: ({camera_pos[0]:.2f}, {camera_pos[1]:.2f}, {camera_pos[2]:.2f})  Yaw: {yaw:.1f}°  Pitch: {pitch:.1f}°"
        info_label.draw()


    def update(dt):
        global camera_pos, yaw, pitch
        global pose_actual, pose_actual_index, space_pressed
        
        forward = [math.cos(math.radians(yaw)), 0, math.sin(math.radians(yaw))]
        right = [-forward[2], 0, forward[0]]

        # Movimiento de cámara
        if keys[pyglet.window.key.W]:
            camera_pos = [camera_pos[i] + forward[i]*speed for i in range(3)]
        if keys[pyglet.window.key.S]:
            camera_pos = [camera_pos[i] - forward[i]*speed for i in range(3)]
        if keys[pyglet.window.key.A]:
            camera_pos = [camera_pos[i] - right[i]*speed for i in range(3)]
        if keys[pyglet.window.key.D]:
            camera_pos = [camera_pos[i] + right[i]*speed for i in range(3)]
        if keys[pyglet.window.key.Q]:
            camera_pos[1] -= speed
        if keys[pyglet.window.key.E]:
            camera_pos[1] += speed
        if keys[pyglet.window.key.LEFT]:
            yaw -= sensitivity
        if keys[pyglet.window.key.RIGHT]:
            yaw += sensitivity
        if keys[pyglet.window.key.UP]:
            pitch += sensitivity
        if keys[pyglet.window.key.DOWN]:
            pitch -= sensitivity
            pitch = max(-89, min(89, pitch))
        
        # Cambiar entre poses con ESPACIO
        if keys[pyglet.window.key.SPACE]:
            if not space_pressed:  # Solo cambiar si no estaba presionado antes
                space_pressed = True
                # Avanzar al siguiente índice
                pose_actual_index = (pose_actual_index + 1) % len(pose_list)
                pose_actual = pose_list[pose_actual_index]
                aplicar_pose(personaje_dict, pose_actual)
                aplicar_camara(Camara_por_pose, pose_actual)
                cambiar_piso(pose_actual)
                print(f"Pose Actual: [{pose_actual_index + 1}/{len(pose_list)}]: {pose_actual}")
        else:
            space_pressed = False  # Resetear cuando se suelta la tecla
    

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()