find_package(Python COMPONENTS Interpreter Development REQUIRED)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(example ext_pybind.cpp)