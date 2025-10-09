from pyglet.gl import *
from ctypes import c_char_p, c_int, create_string_buffer


def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)

    # preparar el source como array de punteros
    src = (c_char_p * 1)(source.encode('utf-8'))
    length = (c_int * 1)(len(source))

    glShaderSource(shader, 1, src, length)
    glCompileShader(shader)

    # revisar si compiló
    status = c_int()
    glGetShaderiv(shader, GL_COMPILE_STATUS, status)
    if not status.value:
        log_len = c_int()
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, log_len)
        buffer = create_string_buffer(log_len.value)
        glGetShaderInfoLog(shader, log_len, None, buffer)
        raise RuntimeError("Shader compile error: " + buffer.value.decode('utf-8'))

    return shader


def create_program(vertex_src, fragment_src):
    vs = compile_shader(vertex_src, GL_VERTEX_SHADER)
    fs = compile_shader(fragment_src, GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vs)
    glAttachShader(program, fs)
    glLinkProgram(program)

    status = c_int()
    glGetProgramiv(program, GL_LINK_STATUS, status)
    if not status.value:
        log_len = c_int()
        glGetProgramiv(program, GL_INFO_LOG_LENGTH, log_len)
        buffer = create_string_buffer(log_len.value)
        glGetProgramInfoLog(program, log_len, None, buffer)
        raise RuntimeError("Program link error: " + buffer.value.decode('utf-8'))

    # limpiar shaders
    glDeleteShader(vs)
    glDeleteShader(fs)

    return program
