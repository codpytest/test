install:
	- if [ "${GITHUB_RUN_OS}" = "Ubuntu" ]; then sudo apt-get update && sudo apt-get install libboost-all-dev; fi

    - if [ "${GITHUB_RUN_OS}" = "Windows" ]; then choco install boost; fi
build:
