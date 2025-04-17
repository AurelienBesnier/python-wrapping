#include <nanobind/nanobind.h>

namespace nb = nanobind;

float square(float x) { return x * x; }

NB_MODULE(libexample, m) {
    m.def("square", &square);
}