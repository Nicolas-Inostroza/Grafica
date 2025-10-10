import math



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
def mat_rotate_z(angle):
    c, s = math.cos(angle), math.sin(angle)
    return (
        c,-s, 0, 0,
        s, c, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1
    )


def mat_mul(a, b):
    out = [0]*16
    for i in range(4):
        for j in range(4):
            out[i*4+j] = sum(a[i*4+k]*b[k*4+j] for k in range(4))
    return tuple(out)