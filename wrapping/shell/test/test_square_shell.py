import pytest
from wrapping.shell import square

@pytest.mark.skip
@pytest.mark.benchmark(group="square", warmup=True)
def test_square_shell(benchmark):
    result = benchmark(square, 2.0)
    assert result == 4.0
