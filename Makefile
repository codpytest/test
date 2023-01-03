install:
# install Boost on Ubuntu
	- if [ "${GITHUB_RUN_OS}" = "Ubuntu" ]; then sudo apt-get update && sudo apt-get install libboost-all-dev; fi
# install Boost on Windows
    - if [ "${GITHUB_RUN_OS}" = "Windows" ]; then choco install boost; fi

build:
# build your code using Boost