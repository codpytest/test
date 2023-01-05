# Author: SMI
cmake_minimum_required(VERSION 3.15)
set(PROJECT_NAME "testing202212" CXX)
project (${PROJECT_NAME})
# set (PROJECT_SOURCE_DECLARATION_DIRECTORY ${PROJECT_SOURCE_DIR}/include)
# set (PROJECT_SOURCE_DEFINITION_DIRECTORY ${PROJECT_SOURCE_DIR}/src)
# set (MAIN_FILE ${PROJECT_SOURCE_DEFINITION_DIRECTORY}/inv.cpp)

# file(GLOB_RECURSE SOURCES RELATIVE ${CMAKE_SOURCE_DIR} "src/*.cpp")


set(CMAKE_CXX_STANDARD 17)
set(Boost_USE_STATIC_LIBS ON)  # only find static libs
set (Boost_USE_MULTITHREADED ON)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set (Boost_USE_STATIC_RUNTIME OFF)
set (BOOST_ALL_DYN_LINK OFF)
set(CMAKE_EXE_LINKER_FLAGS "-static-libgcc -static-libstdc++ -static")


# find_package(Boost 1.74.0 REQUIRED COMPONENTS program_options serialization chrono random) # find Boost
find_package(pybind11 REQUIRED)
# if(Boost_FOUND)
#     # From the offical documentation:
#     # Add include directories to the build. [...] If the SYSTEM option is given,
#     # the compiler will be told the directories are meant as system include
#     # directories on some platforms (signalling this setting might achieve effects
#     # such as the compiler skipping warnings [...])."
#     include_directories(${Boost_INCLUDE_DIRS})

#     # From the offical documentation:
#     # "Specify directories in which the linker will look for libraries. [...] Note
#     # that this command is rarely necessary. Library locations returned by
#     # find_package() and find_library() are absolute paths. Pass these absolute
#     # library file paths directly to the target_link_libraries() command. CMake
#     # will ensure the linker finds them."
#     #link_directories (${Boost_LIBRARY_DIRS})
#     link_libraries(${Boost_LIBRARIES})     # add Boost to link libraries
# endif()

# add_executable(inv ${SOURCES})
# target_link_libraries(inv Boost::boost Boost::chrono) 