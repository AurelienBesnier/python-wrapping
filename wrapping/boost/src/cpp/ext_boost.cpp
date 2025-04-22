#include <boost/python.hpp>
#include <boost/python/class.hpp>
#include <boost/python/operators.hpp>
#include <boost/operators.hpp>

using namespace boost::python;

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

BOOST_PYTHON_MODULE(example)
{
    def("square", square);

    class_<Vector2>("Vector2", init<float,float>())
        .def(self + self)
        .def(self += self)
        .def(self *= float())
        .def(float() * self)
        .def(self * float())
        .def(-self)
        .def("__repr__", &Vector2::to_string);
}