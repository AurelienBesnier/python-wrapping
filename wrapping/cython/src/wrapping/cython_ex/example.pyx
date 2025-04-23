# cython: language_level=3

from libcpp.string cimport string

def square_native(float x):
    return x * x

cdef extern from "square.h":
    float c_square(float x)

def square(x):
    return c_square(x)

cdef extern from "vector2.hpp":
   cdef cppclass Vector2:
       Vector2(float,float) except +
       float x, y
       Vector2 operator+(Vector2)
       string to_string()

cdef class PyVector2:
    cdef Vector2 *c_vect
    def __cinit__(self, float x=0, float y=0):
        self.c_vect = new Vector2(x,y)

    def __dealloc__(self):
        del self.c_vect

    def __add__(PyVector2 left, PyVector2 right):
        return PyVector2.create(left.c_vect[0] + right.c_vect[0])

    def __repr__(self):
        self.c_vect[0].to_string()

    @staticmethod
    cdef create(Vector2 r):
         cdef PyVector2 ret = PyVector2()
         ret.c_vect[0] = r
         return ret
