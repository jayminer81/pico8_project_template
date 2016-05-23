# Pico-8 Project Template
This is an empty Pico-8 project template but with scripts allowing you to separate graphics, music and code and also split the code into multiple files while working on your project.
It comes with a Makefile and a python-script which parses a source-file and allows inclusion of other source-files from it.
When you 'make' your project the graphics and sounds are taken from the file gfxsfx.p8 but no code is picked up from that file so the code-section in that cart can be used to prototype graphics, music and other things.
To include another source-file from the main-source file just type "include <filename>" and if the file exists it will be concatinated into the source, see source.lua for an example.
For now it's not possible to include files from within a file that is getting included, perhaps this will be added in the future.
