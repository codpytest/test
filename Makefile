install:
	- if [ "${GITHUB_RUN_OS}" = "Ubuntu" ]; then sudo apt-get update && sudo apt-get install libboost-all-dev; fi

	- if [ "${GITHUB_RUN_OS}" = "Windows" ]; then choco install boost; fi
build:
    # build on Ubuntu
    - if [ "${GITHUB_RUN_OS}" = "Ubuntu" ]; then $(CXX) -O2 -I/usr/include/boost main.cpp -L/usr/lib/x86_64-linux-gnu -lboost_system -o main; fi
    # build on Windows
    - if [ "${GITHUB_RUN_OS}" = "Windows" ]; then $(CXX) -O2 -I"C:\local\boost_1_72_0" main.cpp -L"C:\local\boost_1_72_0\lib64-msvc-14.2" -lboost_system -o main; fi