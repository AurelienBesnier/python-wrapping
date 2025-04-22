import pytest
from wrapping.nanobind import Vector2


@pytest.mark.benchmark(group="Vector2", warmup=True)
def test_vector_nano(benchmark):
    vec1 = Vector2(2,2)
    vec2 = Vector2(1,1)

    def result(x,y):
        return x + y

    res = benchmark(result, vec1, vec2)
    assert res is not None
