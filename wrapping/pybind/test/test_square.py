from wrapping.nanobind import square

def test_square():
    assert square(2.0) == 4.0