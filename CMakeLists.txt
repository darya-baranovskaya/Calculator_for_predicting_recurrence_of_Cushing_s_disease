cmake_minimum_required(VERSION 3.13)
project(pr2 C)

set(CMAKE_C_STANDARD 11)

add_library(pr2 SHARED library.c library.h)