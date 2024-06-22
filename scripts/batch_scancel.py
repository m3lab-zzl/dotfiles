import os
import sys


def run(cmd: str):
    print("--> ", cmd)
    os.system(cmd)


if len(sys.argv) > 1 and sys.argv[1].startswith("p"):
    cmd = "scontrol update Priority=1 job="
else:
    cmd = "scancel "

yn = input("kill all jobs of current user?" + " (y/n): ")
if yn == "y":
    run("scancel -u $USER")
else:
    a = input("min id: ")
    b = input("max id: ")
    for i in range(int(a), int(b) + 1):
        run(f"{cmd}{i}")
run("squeue")
