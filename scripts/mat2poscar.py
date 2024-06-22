# pip install pymatreader, numpy
import os
import sys

from pymatreader import read_mat

assert sys.version_info >= (3, 6), "Python 3.6+ is required."
matfile = os.path.abspath(
    os.path.expanduser(input("matfile path (/foldername/filename.mat): "))
)

data_dict = read_mat(matfile)
assert isinstance(data_dict, dict), "error reading file, please check your matfile"

latvec = data_dict["domain"]["latvec"]
poses = data_dict["atom"]["xyz"]
if poses.shape == (3,):
    poses = poses.reshape(1, 3)
ele_ind_list = data_dict["atom"]["element"]
if isinstance(ele_ind_list, float):
    ele_ind_list = [int(ele_ind_list)]
else:
    ele_ind_list = ele_ind_list.tolist()  # [1,1,2,2]
ele_species_list = data_dict["element"]["species"]  # ['H','Li']
if isinstance(ele_species_list, str):
    ele_species_list = [ele_species_list]
# count how many atoms for each element
natom_per_element = []
for i, element in enumerate(ele_species_list):
    natom_per_element.append(ele_ind_list.count(i + 1))
# print(f"{natom_per_element=}")

poscar = input("write to ? (/foldername/filename, default to POSCAR): ") or "POSCAR"
with open(poscar, "w") as f:
    f.write(f"data from {matfile}\n")
    f.write("1.0\n")
    f.write(f" {latvec[0][0]:.10f} {latvec[0][1]:.10f} {latvec[0][2]:.10f}\n")
    f.write(f" {latvec[1][0]:.10f} {latvec[1][1]:.10f} {latvec[1][2]:.10f}\n")
    f.write(f" {latvec[2][0]:.10f} {latvec[2][1]:.10f} {latvec[2][2]:.10f}\n")
    f.write(" ".join(ele_species_list) + "\n")
    f.write(" ".join([str(i) for i in natom_per_element]) + "\n")
    f.write("Cartesian\n")
    f.write(
        "\n".join(
            [
                f" {poses[i][0]:.10f} {poses[i][1]:.10f} {poses[i][2]:.10f}"
                for i in range(len(poses))
            ]
        )
    )
print(f"--> {poscar}")
