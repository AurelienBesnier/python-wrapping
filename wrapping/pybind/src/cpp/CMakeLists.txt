find_package(Python COMPONENTS Interpreter Development REQUIRED)

find_package(pybind11 CONFIG REQUIRED)
add_library(libexample MODULE ext_pybind.cpp)
target_link_libraries(libexample PUBLIC pybind11::module pybind11::opt_size pybind11::thin_lto pybind11::windows_extras wp)
pybind11_strip(libexample)
