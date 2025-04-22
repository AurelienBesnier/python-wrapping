try:
    from .libexample import square, Vector2

    __all__ = ["square", "Vector2"]

except:
    print("could not import c++ library")
