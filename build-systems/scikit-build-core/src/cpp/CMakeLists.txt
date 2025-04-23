find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Detect the installed nanobind package and import it into CMake
execute_process(
COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(libexample LTO ext_nano.cpp)
target_link_libraries(libexample PUBLIC wn)