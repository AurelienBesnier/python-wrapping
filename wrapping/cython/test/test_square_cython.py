import pytest
from wrapping.cython_ex import square_native, square


@pytest.mark.benchmark(group="square", warmup=True)
def test_square_native_cython(benchmark):
    result = benchmark(square_native, 2.0)
    assert result == 4.0

@pytest.mark.benchmark(group="square", warmup=True)
def test_square_cython(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0