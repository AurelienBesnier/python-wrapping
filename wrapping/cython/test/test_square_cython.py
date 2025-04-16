import pytest
from wrapping.cython_ex import square

@pytest.mark.benchmark(warmup=True)
def test_square_cython(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0
