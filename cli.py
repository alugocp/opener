#!/usr/bin/env python
from sys import argv
import opener as o

if len(argv)==1:
    print("Usage: opener ( open | print | skip-hidden | ignore )")
    exit()

options=o.get_options()

if argv[1]=="open":
    if len(argv)==2: print("Name a project(s) to open")
    else:
        for p in range(2,len(argv)): o.open_project(options,argv[p])

elif argv[1]=="print":
    if len(argv)==2: o.print_sites(options)
    else: print("Too many arguments")

elif argv[1]=="skip-hidden":
    if len(argv)==2: print("Expecting 'y' or 'n'")
    elif len(argv)==3: o.ignore_hidden(options,"y" in argv[2])
    else: print("Too many arguments")

elif argv[1]=="ignore":
    if len(argv)==2: print("Name a path(s) to ignore")
    else:
        for p in range(2,len(argv)): o.add_ignore(options,argv[p])

else: print("Unknown command")

o.save_options(options)
