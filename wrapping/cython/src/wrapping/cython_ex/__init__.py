try:
    from .example import square, square_native, PyVector2

    __all__ = ["square", "square_native", "PyVector2"]

except:
    print("could not import c++ library")
