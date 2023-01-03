cmake_minimum_required(VERSION 3.12)

project(test)

# set(Boost_USE_STATIC_LIBS ON)

# find_package(Boost REQUIRED thread)

# message("Debug:")
# message("${Boost_INCLUDE_DIRS}")
# message("${Boost_LIBRARIES}")

# include_directories(${Boost_INCLUDE_DIRS})

install:
ifeq ($(OS),Windows_NT)
  choco install boost
else
  sudo apt-get update && sudo apt-get install libboost-all-dev
endif

# add_executable(test main.cpp)
# target_link_libraries(test ${Boost_LIBRARIES})
# target_compile_definitions(test PRIVATE -DBOOST_NO_AUTO_PTR -DBOOST_ALL_NO_LIB)