install:
ifeq ($(OS),Windows_NT)
  choco install boost
else
  sudo apt-get update && sudo apt-get install libboost-all-dev
endif