#!/usr/bin/env python

# Parses a file and types it to screen, if it encounters the word "include"
# followed by a filename at the beginning of a line that entire file printed
# instead of the include-line.

import sys
import os.path

if len(sys.argv) != 2:
    sys.exit("Usage: " + os.path.basename(sys.argv[0]) + " <sourcefile>")

if not os.path.exists(sys.argv[1]):
    sys.exit("File " + sys.argv[1] + " not found.")

sourceFile = file(sys.argv[1])
for line in sourceFile:
    lineStripped = line.strip()
    if not lineStripped.startswith("include"):
        print line,
    else:
        lineInclude = lineStripped.split()
        if not os.path.exists(lineInclude[1]):
                    sys.exit("Included file " + lineInclude[1] + " not found.")
        includeFile = file(lineInclude[1])
        if not os.path.exists(lineInclude[1]):
            sys.exit("Included file " + lineInclude[1] + " not found.")
        for incLine in includeFile:
            print incLine,
        