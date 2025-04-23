import pytest
from wrapping.cython_ex import PyVector2


@pytest.mark.benchmark(group="Vector2", warmup=True)
def test_vector_cython(benchmark):
    vec1 = PyVector2(2,2)
    vec2 = PyVector2(1,1)

    def result(x,y):
        return x + y

    res = benchmark(result, vec1, vec2)
    assert res is not None
