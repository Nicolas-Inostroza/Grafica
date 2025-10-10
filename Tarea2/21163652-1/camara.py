import math




"""
perspective :: float,float,float,float -> list
4 valores para mopdificar la perspectiva de la camara.
El fovy permite ajustar el angulo de vista dando un efecto de ojo de pez a la camara.
Aspect es el tama;o de la pantalla donde aplicar la camara.
Near permite decidir la distancia minima donde aparecera algo en la camara entre mayor sea mas lejos dehbe estar algo para aparecer en camara.
Far decide la distancia maxima que puede ver la camara todo lo que este fuera de este rango no aparecera.
"""
def perspective(fovy, aspect, near, far):
    f = 1.0 / math.tan(fovy / 2.0)
    return (
        f / aspect, 0, 0, 0,
        0, f, 0, 0,
        0, 0, (far + near) / (near - far), -1,
        0, 0, (2 * far * near) / (near - far), 0
    )


"""
look_at :: list,list,list -> list
Toma tres listas, la primera es la posicion actual de la camara, la posicion objetivo y una lista que aumenta en 1 la altura de la camara
"""
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


