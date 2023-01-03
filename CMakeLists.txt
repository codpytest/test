cmake_minimum_required(VERSION 3.14)
project(testing)

# find Boost
find_package(Boost REQUIRED COMPONENTS system)

# add Boost to include directories
include_directories(${Boost_INCLUDE_DIRS})

# add Boost to link libraries
link_libraries(${Boost_LIBRARIES})

# add executable
# add_executable(testing main.cpp)