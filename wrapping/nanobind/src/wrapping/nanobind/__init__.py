try:
    from .libexample import square

    __all__ = ["square"]

except:
    print("could not import c++ library")