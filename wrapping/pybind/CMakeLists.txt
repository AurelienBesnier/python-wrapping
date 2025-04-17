cmake_minimum_required(VERSION 3.20)
project(wrapping_pybind LANGUAGES CXX)
add_subdirectory("src/cpp/")
add_library(wp INTERFACE src/cpp/ext_pybind.cpp)

set_target_properties(wp
        PROPERTIES
        CXX_STANDARD 23
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS YES
        )

find_package(Python COMPONENTS Interpreter Development REQUIRED)
# building lib
install(TARGETS example
        COMPONENT python
        LIBRARY DESTINATION "${CMAKE_SOURCE_DIR}/src/wrapping/pybind/")