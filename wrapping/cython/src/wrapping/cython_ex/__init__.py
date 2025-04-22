try:
    from .example import square, square_native

    __all__ = ["square", "square_native"]

except:
    print("could not import c++ library")
