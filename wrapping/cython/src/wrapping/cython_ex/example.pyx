# cython: language_level=3

def square_native(float x):
    return x * x


cdef extern from "square.h":
    float c_square(float x)

def square(x):
    return c_square(x)

# cdef extern from "vector2.hpp":
#    cdef cppclass Vector2:
#        Vector2(float,float) except +
#        float x, y