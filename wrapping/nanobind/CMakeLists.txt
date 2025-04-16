cmake_minimum_required(VERSION 3.20)
project(wrapping_nanobind LANGUAGES CXX)

# OpenMP
if(APPLE)
    set(CMAKE_CXX_COMPILER clang++)
    set(CMAKE_CXX_FLAGS "${CXXFLAGS} -D_LIBCPP_DISABLE_AVAILABILITY")

    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang\$")
        set(OpenMP_CXX_FLAGS "-Xpreprocessor -fopenmp")
        set(OpenMP_CXX_LIB_NAMES "omp")
        set(OpenMP_omp_LIBRARY omp)
    endif()
endif()

# pm(photon_mapping)
add_subdirectory("src/cpp/")
add_library(wn INTERFACE src/cpp/ext_nano.cpp)

set_target_properties(wn
        PROPERTIES
        CXX_STANDARD 23
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS YES
        )



# wrapper

# building lib
find_package(Python COMPONENTS Interpreter Development REQUIRED)
# Detect the installed nanobind package and import it into CMake
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)

install(TARGETS libexample
        COMPONENT python
        LIBRARY DESTINATION "${CMAKE_SOURCE_DIR}/src/wrapping/nanobind/")