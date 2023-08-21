#!/usr/bin/python3
import sys

# Check if there is only one argument:
if len(sys.argv) != 2:
    print("Usage: include only a pdb file")

# Check if first argument is a readable file name:
elif len(sys.argv) == 2:
    # Open file, so it closes automatically with "with":
    try:
        with open(sys.argv[1]) as f:
            # Check if file is readable:
            if not f.readable():
                print(f"{sys.argv[1]} should be a readable file name")
            else:
                # Loop through all the lines in file:
                for line in f.readlines():
                    # Get a hold of the lines that start with ATOM:
                    if line.startswith("ATOM"):
                        # Turn the desired line into a list to access values:
                        lst = line.split()
                        # Output desired information by accessing list:
                        print(f"\nAtom serial number: {lst[1]}")
                        print(f"\nX coordinates: {lst[6]}")
                        print(f"\nY coordinates: {lst[7]}")
                        print(f"\nZ coordinates: {lst[8]}")

    # Handling error raised when providing a non-existent file:
    except FileNotFoundError:
        print("The file passed does not exist")
        sys.exit()
    # Handling error raised when providing a file without reading permission:
    except PermissionError:
        print("You don't have the appropriate permission to read this file")
        sys.exit()

