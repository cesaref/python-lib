cmake_minimum_required(VERSION 3.15)
project(python_lib VERSION 1.0.0 LANGUAGES CXX)

# Create interface library for header-only CHOC
add_library(python_lib INTERFACE)

# Set include directories
target_include_directories(python_lib INTERFACE install/include/python3.13)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    target_link_libraries(python_lib INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/install/lib/libpython3.13.a)
endif()