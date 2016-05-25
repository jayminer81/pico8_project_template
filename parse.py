#!/usr/bin/env python

# Parses a file and types it to screen, if it encounters the word "include"
# followed by a filename at the beginning of a line that entire file printed
# instead of the include-line.

import sys
import os.path

optimize = False
if len(sys.argv) > 2:
    if sys.argv[2]=="--optimize":
        optimize = True

if len(sys.argv) != 2 and not optimize:
    sys.exit("Usage: " + os.path.basename(sys.argv[0]) + " <sourcefile> [-optimize]")

if not os.path.exists(sys.argv[1]):
    sys.exit("File " + sys.argv[1] + " not found.")

sourceFile = file(sys.argv[1])
for line in sourceFile:
    lineStripped = line.strip()
    if lineStripped.startswith("include"):
        lineInclude = lineStripped.split()
        if not os.path.exists(lineInclude[1]):
                    sys.exit("Included file " + lineInclude[1] + " not found.")
        includeFile = file(lineInclude[1])
        if not os.path.exists(lineInclude[1]):
            sys.exit("Included file " + lineInclude[1] + " not found.")
        for incLine in includeFile:
            incStripped = incLine.strip()
            if incStripped.startswith("--") and optimize:
                pass
            else:
                if optimize:
                    if not incStripped=="":
                        print incStripped
                else:
                    print incLine,
    elif lineStripped.startswith("--") and optimize:
        pass
    else:
        if optimize:
            if not lineStripped=="":
                print lineStripped
        else:
            print line,
