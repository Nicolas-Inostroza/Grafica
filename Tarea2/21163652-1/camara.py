import math



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