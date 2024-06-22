# pip install pymatreader, numpy, scipy
import json
import os
import sys

import numpy as np
from pymatreader import read_mat
from scipy.sparse import csc_matrix

assert sys.version_info >= (3, 6), "Python 3.6+ is required."


def clean_value(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    elif isinstance(value, csc_matrix):
        if verbose:
            return value.toarray().tolist()
        else:
            return np.shape(value.toarray())
    elif isinstance(value, list):
        return [clean_value(v) for v in value]
    else:
        return value


def clean_dict(mat: dict):
    """
    - mat may contain nested dict
    - keys startswith "__" are not needed
    - np.ndarray and scipy.sparse.csc_matrix should be converted to list so that it can be saved as json/yaml
    """
    new_dict = {}
    for key, value in mat.items():
        if key.startswith("__"):
            continue
        if isinstance(value, dict):
            value = clean_dict(value)
        else:
            value = clean_value(value)
        new_dict[key] = value

    return new_dict


def mat2json(matfile: str, jsonfile: str):
    mat = read_mat(matfile)
    assert isinstance(mat, dict), "error reading file, please check your matfile"
    clean_mat = clean_dict(mat)

    json.dump(clean_mat, open(jsonfile, "w"))
    print(f"--> {os.path.abspath(jsonfile)}")


if __name__ == "__main__":
    matfile = os.path.abspath(
        os.path.expanduser(input("matfile path (/foldername/filename.mat): "))
    )
    yn = input("write array values or just show its shape? (y/n): ")
    if yn == "y":
        verbose = True
    else:
        verbose = False

    jsonfile = matfile[:-4] + ".json"
    mat2json(matfile, jsonfile)
