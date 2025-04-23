#include <nanobind/nanobind.h>
#include <nanobind/operators.h>

namespace nb = nanobind;

float square(float x) { return x * x; }


NB_MODULE(libexample, m) {
    m.def("square", &square);
}