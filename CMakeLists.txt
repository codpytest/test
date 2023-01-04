cmake_minimum_required(VERSION 3.15)
project(testing)


set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_CXX_STANDARD_REQUIRED True)
# set(CMAKE_EXE_LINKER_FLAGS "-static-libgcc -static-libstdc++ -static")

# find Boost
find_package(Boost 1.72.0 COMPONENTS REQUIRED program_options serialization system)
include_directories(${Boost_INCLUDE_DIRS})
# add Boost to link libraries
link_libraries(${Boost_LIBRARIES})

# add_executable(testing ${FILES})

# target_link_libraries(testing ${Boost_LIBRARIES} pthread)
# add_executable(testing main.cpp)