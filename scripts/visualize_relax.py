# pip install numpy
import os
import sys

import numpy as np

assert sys.version_info >= (3, 6), "Python 3.6+ is required."


rt = input("relaxationprocess.txt file location (/foldername/relaxationprocess.txt): ")
na = int(input("number of atoms (check your xyz file): "))
lat = input("lattice matrix (3x3=9, separate by space): ")

with open(os.path.abspath(os.path.expanduser(rt))) as rp:
    lines = rp.readlines()
    elements = []
    poses = []
    for i, line in enumerate(lines):
        if i % (na + 8) in [0, 1, 2, 3, 4, 5, na + 6, na + 7]:
            continue
        ll = line.split()
        elements.append(ll[1].removesuffix(":"))
        poses.append([float(ll[2]), float(ll[3]), float(ll[4])])

    nimages = len(elements) // na
    print(f" found {nimages} images")
    elements = np.split(np.array(elements), nimages)
    poses = np.split(np.array(poses) * 0.52917721067, nimages)

out = (
    input("write to ? (/foldername/filename.xyz, defaults to traj.xyz): ") or "traj.xyz"
)
with open(os.path.abspath(os.path.expanduser(out)), "w") as f:
    for i, (ele, pos) in enumerate(zip(elements, poses)):
        f.write(f"{len(ele)}\n")
        f.write(f'Lattice="{lat}" Properties=species:S:1:pos:R:3\n')
        for j in range(na):
            f.write(f"{ele[j]} {pos[j][0]} {pos[j][1]} {pos[j][2]}\n")
print(f"--> {out}")
