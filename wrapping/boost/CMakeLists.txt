cmake_minimum_required(VERSION 3.20)
project(wrapping_boost LANGUAGES CXX)

find_package(PythonInterp)
find_package(PythonLibs)

find_package(Boost REQUIRED COMPONENTS python${PYTHON_VERSION_SUFFIX})

message("${PYTHON_INCLUDE_DIRS}")

include_directories(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
link_libraries(${Boost_LIBRARIES} ${PYTHON_LIBRARIES})



message(STATUS "PYTHON_LIBRARIES = ${PYTHON_LIBRARIES}")
message(STATUS "PYTHON_EXECUTABLE = ${PYTHON_EXECUTABLE}")
message(STATUS "PYTHON_INCLUDE_DIRS = ${PYTHON_INCLUDE_DIRS}")
message(STATUS "Boost_LIBRARIES = ${Boost_LIBRARIES}")

add_subdirectory("src/cpp/")
add_library(wb SHARED src/cpp/ext_boost.cpp)


set_target_properties(wb
        PROPERTIES
        CXX_STANDARD 23
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS YES
        )

# building lib
install(TARGETS example
        COMPONENT python
        LIBRARY DESTINATION "${CMAKE_SOURCE_DIR}/src/wrapping/boost/")