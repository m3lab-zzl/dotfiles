# pip install h5py numpy
import os
import sys

import h5py
import numpy as np

args = sys.argv
np.set_printoptions(threshold=sys.maxsize)


def print_value(h5file, key):
    print()
    absfile = os.path.abspath(h5file)
    with h5py.File(absfile, "r") as f:
        if key in f.keys():
            print("====== %s ======" % absfile)
            value = np.array(f[key])
            if len(value) > 100:
                print("shape: ", value.shape)
                yn = input("print all? (y/n): ")
                if yn.lower().startswith("y"):
                    print("--> ", value)
            else:
                print("--> ", value)
    print()


# python whatis.py <h5file> <key>
if len(args) == 1:
    h5file = input("h5file: ")
    key = input("key: ")
    print_value(h5file, key)

elif len(args) == 2:
    h5file = args[1]
    key = input("key: ")
    print_value(h5file, key)

elif len(args) == 3:
    h5file = args[1]
    key = args[2]
    print_value(h5file, key)

else:
    print("Usage: python whatis.py <h5file> <key>")
    sys.exit(1)
