import pytest
from wrapping.boost import square

@pytest.mark.benchmark(warmup=True)
def test_square_boost(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0
