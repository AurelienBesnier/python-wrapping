#include <boost/python.hpp>
using namespace boost::python;

float square(float x) { return x * x; }

BOOST_PYTHON_MODULE(example)
{
    def("square", square);
}