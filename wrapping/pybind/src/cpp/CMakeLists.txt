find_package(Python COMPONENTS Interpreter Development REQUIRED)

find_package(pybind11 CONFIG REQUIRED)
add_library(libexample MODULE ext_pybind.cpp)
target_link_libraries(libexample PUBLIC pybind11::module wp)
pybind11_strip(libexample)
