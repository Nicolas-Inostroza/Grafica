import math
import pyglet
from pyglet import gl

window = pyglet.window.Window(800, 600, "Parent-Child Sphere-Cylinder", resizable=True)

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

# --- Geometry generators ---
def create_sphere(radius=1.0, slices=32, stacks=16):
    vertices = []
    indices = []
    for i in range(stacks + 1):
        lat = math.pi * (-0.5 + float(i) / stacks)
        z = radius * math.sin(lat)
        r = radius * math.cos(lat)
        for j in range(slices + 1):
            lon = 2 * math.pi * float(j) / slices
            x = r * math.cos(lon)
            y = r * math.sin(lon)
            vertices += [x, y, z]
    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1
            indices += [first, second, first + 1,
                        second, second + 1, first + 1]
    return vertices, indices

def create_cylinder(radius=0.2, height=2.0, slices=32):
    vertices = []
    indices = []
    half = height / 2.0
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices += [x, y, -half]
        vertices += [x, y,  half]
    for i in range(0, slices * 2, 2):
        indices += [
            i, i+1, (i+2) % (2*(slices+1)),
            i+1, (i+3) % (2*(slices+1)), (i+2) % (2*(slices+1))
        ]
    return vertices, indices

# Sphere and cylinder vlist
vertices, indices = create_sphere()
sphere_vlist = shader.vertex_list_indexed(len(vertices)//3, gl.GL_TRIANGLES, indices,
                                          position=(('f', 3), vertices))
cyl_vertices, cyl_indices = create_cylinder()
cylinder_vlist = shader.vertex_list_indexed(len(cyl_vertices)//3, gl.GL_TRIANGLES, cyl_indices,
                                            position=(('f', 3), cyl_vertices))

# --- Matrix helpers ---
def mat_identity():
    return (
        1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        0,0,0,1
    )

def mat_translate(x,y,z):
    return (
        1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        x,y,z,1
    )

def mat_rotate_y(angle):
    c = math.cos(angle)
    s = math.sin(angle)
    return (
        c,0,s,0,
        0,1,0,0,
        -s,0,c,0,
        0,0,0,1
    )

def mat_rotate_x(angle):
    c, s = math.cos(angle), math.sin(angle)
    return (
        1, 0, 0, 0,
        0, c,-s, 0,
        0, s, c, 0,
        0, 0, 0, 1
    )


def mat_mul(a, b):
    out = [0]*16
    for i in range(4):
        for j in range(4):
            out[i*4+j] = sum(a[i*4+k]*b[k*4+j] for k in range(4))
    return tuple(out)

# --- Camera setup ---
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

# --- Camera controls ---
camera_pos = [0, 0, 6]
yaw, pitch = 0, 0
speed = 0.1
sensitivity = 2.0

# --- Sphere rotation control ---
sphere_rotation = 0.0

def tarea():
    global sphere_rotation

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

        # esfera (padre, con rotación)
        model_sphere = mat_rotate_y(sphere_rotation)
        shader["model"] = model_sphere
        shader["color"] = (0.2, 0.6, 1.0)
        sphere_vlist.draw(gl.GL_TRIANGLES)

        # cilindro (hijo → se transforma con la esfera)
        initial_rot = mat_rotate_y(math.radians(90))  # 45° inicial
        model_cyl = mat_mul(initial_rot,mat_translate(2, 0, 0))
        model_cyl = mat_mul(model_cyl,model_sphere)

        shader["model"] = model_cyl
        shader["color"] = (1.0, 0.5, 0.2)
        cylinder_vlist.draw(gl.GL_TRIANGLES)

    def update(dt):
        global camera_pos, yaw, pitch, sphere_rotation
        forward = [
            math.cos(math.radians(yaw)), 0, math.sin(math.radians(yaw))
        ]
        right = [-forward[2], 0, forward[0]]

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

        # ROTACIÓN con la barra espaciadora
        if keys[pyglet.window.key.SPACE]:
            sphere_rotation += 0.05

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
