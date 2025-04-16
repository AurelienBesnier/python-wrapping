import pytest
from wrapping.fortran import square

@pytest.mark.benchmark(warmup=True)
def test_square_fortran(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0
