import pytest
from wrapping.nanobind import square


@pytest.mark.benchmark(group="square", warmup=True)
def test_square_nano(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0
