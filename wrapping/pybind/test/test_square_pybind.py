import pytest
from wrapping.pybind import square

@pytest.mark.benchmark(warmup=True)
def test_square_pybind(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0
