cmake_minimum_required(VERSION 3.20)
project(wrapping_shell LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

add_subdirectory("src/cpp/")

install(TARGETS square
        DESTINATION "$ENV{CONDA_PREFIX}/bin")