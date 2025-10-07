import math
import pyglet
from pyglet import gl

from .geometry import create_sphere, create_cylinder, create_cube
from .trasformaciones import mat_identity, mat_translate, mat_rotate_y, mat_rotate_x, mat_mul
from .nodo import Nodo
from .camara import perspective, look_at
from .personaje import crear_personaje
from .poses import apply_pose

window = pyglet.window.Window(800, 600, "Personaje Articulado", resizable=True)

# --- Shader ---
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

pos_torso = [0.0, 0.0, 0.0]  # Posición del torso
personaje_dict, cuerpo, torso = crear_personaje(shader)
current_pose = "neutral"
apply_pose(personaje_dict, current_pose)  # Aplicar pose inicial


def tarea():
    global current_pose  # Agregar current_pose aquí

    keys = pyglet.window.key.KeyStateHandler()
    window.push_handlers(keys)
    

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

        # Dibujar todo el árbol - CAMBIO IMPORTANTE: pasar None para que sea la raíz
        torso.draw(None)


    def update(dt):
        global camera_pos, yaw, pitch
        global current_pose  # Ya no necesitas angulo_torso_y, angulo_torso_x, pos_torso
        
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
        
        # Cambio de poses
        if keys[pyglet.window.key._1]:
            if current_pose != "neutral":
                current_pose = "neutral"
                apply_pose(personaje_dict, current_pose)
                print(f"Applied pose: {current_pose}")
        if keys[pyglet.window.key._2]:
            if current_pose != "t_pose":
                current_pose = "t_pose"
                apply_pose(personaje_dict, current_pose)
                print(f"Applied pose: {current_pose}")
        if keys[pyglet.window.key._3]:
            if current_pose != "walking":
                current_pose = "walking"
                apply_pose(personaje_dict, current_pose)
                print(f"Applied pose: {current_pose}")
        if keys[pyglet.window.key._4]:
            if current_pose != "sitting":
                current_pose = "sitting"
                apply_pose(personaje_dict, current_pose)
                print(f"Applied pose: {current_pose}")
        if keys[pyglet.window.key._5]:
            if current_pose != "waving":
                current_pose = "waving"
                apply_pose(personaje_dict, current_pose)
                print(f"Applied pose: {current_pose}")

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()