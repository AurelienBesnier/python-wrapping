import sys

try:
    from .example import square, Vector2

    __all__ = ["square", "Vector2"]

except Exception as e:
    import traceback

    traceback.print_exception(e)
    print("could not import c++ library", file=sys.stderr)
