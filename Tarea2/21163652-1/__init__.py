import math
import pyglet
from pyglet import gl
from .geometry import create_sphere, create_cylinder, create_cube
from .trasformaciones import mat_identity, mat_translate, mat_rotate_y, mat_rotate_x, mat_mul
from .nodo import Nodo

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

# --- Crear geometrías ---
verts_sphere, inds_sphere = create_sphere(radius=0.5)
vlist_sphere = shader.vertex_list_indexed(len(verts_sphere)//3, gl.GL_TRIANGLES, inds_sphere,
                                          position=(('f', 3), verts_sphere))

verts_cube, inds_cube = create_cube(size=1.3)
vlist_cube = shader.vertex_list_indexed(len(verts_cube)//3, gl.GL_TRIANGLES, inds_cube,
                                        position=(('f', 3), verts_cube))

# Brazos: cilindros VERTICALES (eje Y) que apuntan hacia abajo naturalmente
verts_arm, inds_arm = create_cylinder(radius=0.15, height=0.6, axis='y')
vlist_arm = shader.vertex_list_indexed(len(verts_arm)//3, gl.GL_TRIANGLES, inds_arm,
                                       position=(('f', 3), verts_arm))

verts_antebrazo, inds_antebrazo = create_cylinder(radius=0.15, height=0.6, axis='y',rotation=( -25, 'x'))
vlist_antebrazo = shader.vertex_list_indexed(len(verts_antebrazo)//3, gl.GL_TRIANGLES, inds_antebrazo,
                                       position=(('f', 3), verts_antebrazo))

# Piernas: cilindros VERTICALES (eje Y)
verts_leg, inds_leg = create_cylinder(radius=0.2, height=1.0, axis='y')
vlist_leg = shader.vertex_list_indexed(len(verts_leg)//3, gl.GL_TRIANGLES, inds_leg,
                                       position=(('f', 3), verts_leg))

verts_foot, inds_foot = create_cube(size=0.4)
vlist_foot = shader.vertex_list_indexed(len(verts_foot)//3, gl.GL_TRIANGLES, inds_foot,
                                        position=(('f', 3), verts_foot))

# --- CONSTRUIR PERSONAJE ---
# 1. Torso (raíz) - CUBO
torso = Nodo("Torso")
torso.model = vlist_cube
torso.shader = shader
torso.color = (0.3, 0.5, 0.8)
torso.transformacion_local = mat_identity()  # Posición local fija
torso.set_transformacion(mat_identity())

# 2. Cabeza (hija del torso)
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
antebrazo_izq = Nodo("antebrazo_izq")
antebrazo_izq.model = vlist_antebrazo
antebrazo_izq.shader = shader
antebrazo_izq.color = (0.9, 0.7, 0.5)
# SOLO posición, la geometría ya está orientada correctamente
antebrazo_izq.transformacion_local = mat_translate(0, -0.6, 0.2)
brazo_izq.agregar_hijo(antebrazo_izq)


# 4. Brazo Derecho
brazo_der = Nodo("Brazo_Der")
brazo_der.model = vlist_arm
brazo_der.shader = shader
brazo_der.color = (0.9, 0.7, 0.5)
brazo_der.transformacion_local = mat_translate(1.0, 0.5, 0)
torso.agregar_hijo(brazo_der)

# 3. Antebrazo Izquierdo
antebrazo_der = Nodo("antebrazo_der")
antebrazo_der.model = vlist_antebrazo
antebrazo_der.shader = shader
antebrazo_der.color = (0.9, 0.7, 0.5)
# SOLO posición, la geometría ya está orientada correctamente
antebrazo_der.transformacion_local = mat_translate(0, -0.6, 0.2)
brazo_der.agregar_hijo(antebrazo_der)

# 5. Pierna Izquierda
pierna_izq = Nodo("Pierna_Izq")
pierna_izq.model = vlist_leg
pierna_izq.shader = shader
pierna_izq.color = (0.2, 0.3, 0.6)
pierna_izq.transformacion_local = mat_translate(-0.4, -1.3, 0)
torso.agregar_hijo(pierna_izq)

# 6. Pie Izquierdo (hijo de pierna izquierda)
pie_izq = Nodo("Pie_Izq")
pie_izq.model = vlist_foot
pie_izq.shader = shader
pie_izq.color = (0.1, 0.1, 0.1)
pie_izq.transformacion_local = mat_mul(mat_translate(0, -0.7, 0.2), mat_rotate_x(math.radians(0)))
pierna_izq.agregar_hijo(pie_izq)

# 7. Pierna Derecha
pierna_der = Nodo("Pierna_Der")
pierna_der.model = vlist_leg
pierna_der.shader = shader
pierna_der.color = (0.2, 0.3, 0.6)
pierna_der.transformacion_local = mat_translate(0.4, -1.3, 0)
torso.agregar_hijo(pierna_der)

# 8. Pie Derecho (hijo de pierna derecha)
pie_der = Nodo("Pie_Der")
pie_der.model = vlist_foot
pie_der.shader = shader
pie_der.color = (0.1, 0.1, 0.1)
pie_der.transformacion_local = mat_mul(mat_translate(0, -0.7, 0.2), mat_rotate_x(math.radians(0)))
pierna_der.agregar_hijo(pie_der)

# --- Cámara ---
def perspective(fovy, aspect, near, far):
    f = 1.0 / math.tan(fovy / 2.0)
    return (
        f / aspect, 0, 0, 0,
        0, f, 0, 0,
        0, 0, (far + near) / (near - far), -1,
        0, 0, (2 * far * near) / (near - far), 0
    )

def look_at(eye, target, up):
    f = [(t - e) for t, e in zip(target, eye)]
    flen = math.sqrt(sum(x*x for x in f))
    f = [x/flen for x in f]
    ulen = math.sqrt(sum(x*x for x in up))
    up = [x/ulen for x in up]
    s = [f[1]*up[2] - f[2]*up[1],
         f[2]*up[0] - f[0]*up[2],
         f[0]*up[1] - f[1]*up[0]]
    u = [s[1]*f[2] - s[2]*f[1],
         s[2]*f[0] - s[0]*f[2],
         s[0]*f[1] - s[1]*f[0]]
    return (
        s[0], u[0], -f[0], 0,
        s[1], u[1], -f[1], 0,
        s[2], u[2], -f[2], 0,
        -sum(s[i]*eye[i] for i in range(3)),
        -sum(u[i]*eye[i] for i in range(3)),
        sum(f[i]*eye[i] for i in range(3)),
        1
    )

projection = perspective(math.radians(65), window.width / window.height, 0.1, 100.0)

# --- Controles ---
camera_pos = [0, 0, 6]
yaw, pitch = -90, 0
speed = 0.1
sensitivity = 2.0

pos_torso = [0.0, 0.0, 0.0]  # Posición del torso

def tarea():
    global angulo_torso_y, angulo_torso_x, pos_torso

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

        # Aplicar transformaciones al torso (combina traslación y rotación)
        # IMPORTANTE: Primero rota, luego traslada
        torso.set_transformacion(
                mat_translate(pos_torso[0], pos_torso[1], pos_torso[2])
        )

        # Dibujar todo el árbol
        draw_node(torso, mat_identity())

    def draw_node(nodo, parent_matrix):
        model_matrix = mat_mul(parent_matrix, nodo.transformacion)
        shader["model"] = model_matrix
        shader["color"] = nodo.color
        if nodo.model:
            nodo.model.draw(gl.GL_TRIANGLES)
        for hijo in nodo.hijos:
            draw_node(hijo, model_matrix)

    def update(dt):
        global camera_pos, yaw, pitch
        global angulo_torso_y, angulo_torso_x, pos_torso
        
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

        # ===== CONTROLES DEL TORSO (TODO SE MUEVE JUNTO) =====
        # Mover torso adelante/atrás con I/K
        if keys[pyglet.window.key.I]:
            pos_torso[2] -= 0.05  # Adelante
        if keys[pyglet.window.key.K]:
            pos_torso[2] += 0.05  # Atrás
            
        # Mover torso arriba/abajo con U/J
        if keys[pyglet.window.key.U]:
            pos_torso[1] += 0.05  # Arriba
        if keys[pyglet.window.key.J]:
            pos_torso[1] -= 0.05  # Abajo
            
        # Mover torso izquierda/derecha con H/L
        if keys[pyglet.window.key.H]:
            pos_torso[0] -= 0.05  # Izquierda
        if keys[pyglet.window.key.L]:
            pos_torso[0] += 0.05  # Derecha

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()