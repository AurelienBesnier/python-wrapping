try:
    from .example import square

    __all__ = ["square"]

except Exception as e:
    import traceback
    traceback.print_exception(e)
    print("could not import c++ library")