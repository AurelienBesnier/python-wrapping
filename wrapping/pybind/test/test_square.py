import pytest
from wrapping.nanobind import square

@pytest.mark.benchmark(warmup=True)
def test_square(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0