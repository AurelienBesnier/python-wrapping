#include <nanobind/nanobind.h>
#include <nanobind/operators.h>

namespace nb = nanobind;

float square(float x) { return x * x; }

class Vector2 {
public:
    Vector2(float x, float y) : x(x), y(y) { }

    Vector2 operator+(const Vector2 &v) const { return Vector2(x + v.x, y + v.y); }
    Vector2 operator*(float value) const { return Vector2(x * value, y * value); }
    Vector2 operator-() const { return Vector2(-x, -y); }
    Vector2& operator+=(const Vector2 &v) { x += v.x; y += v.y; return *this; }
    Vector2& operator*=(float v) { x *= v; y *= v; return *this; }

    friend Vector2 operator*(float f, const Vector2 &v) {
        return Vector2(f * v.x, f * v.y);
    }

    std::string to_string() const {
        return "[" + std::to_string(x) + ", " + std::to_string(y) + "]";
    }
private:
    float x, y;
};


NB_MODULE(libexample, m) {
    m.def("square", &square);

    nb::class_<Vector2>(m, "Vector2")
        .def(nb::init<float, float>())
        .def(nb::self + nb::self)
        .def(nb::self += nb::self)
        .def(nb::self *= float())
        .def(float() * nb::self)
        .def(nb::self * float())
        .def(-nb::self)
        .def("__repr__", &Vector2::to_string);
}