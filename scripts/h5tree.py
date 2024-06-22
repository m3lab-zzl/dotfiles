# pip install h5py
try:
    import h5py
except ImportError:
    import os

    os.system("pip install h5py")
    import h5py

from os.path import abspath


def h5_tree(val, pre=""):
    items = len(val)
    for key, val in val.items():
        items -= 1
        if items == 0:
            # the last item
            if type(val) == h5py._hl.group.Group:
                print(pre + "└── " + key)
                h5_tree(val, pre + "    ")
            else:
                print(pre + "└── " + key + " (%d)" % len(val))
        else:
            if type(val) == h5py._hl.group.Group:
                print(pre + "├── " + key)
                h5_tree(val, pre + "│   ")
            else:
                print(pre + "├── " + key + " (%d)" % len(val))


if __name__ == "__main__":
    filename_hdf = input("filepath:")
    with h5py.File(filename_hdf, "r") as hf:
        print("HDF5 file: %s" % abspath(filename_hdf))
        h5_tree(hf)
