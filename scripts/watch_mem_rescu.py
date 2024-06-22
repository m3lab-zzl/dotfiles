import os
import sys
import time

max_mem_usage = 0
while True:
    total_mem = int(os.popen("free").readlines()[1].split()[1])
    used_mem = int(os.popen("free").readlines()[1].split()[2])
    sys.stdout.write("\r used: %.2f GB" % (used_mem / 1024 / 1024))
    sys.stdout.flush()
    time.sleep(0.1)
    if used_mem > max_mem_usage:
        max_mem_usage = used_mem

    if len(os.popen("ps -ef | grep rescu").readlines()) == 2:
        print("\nrescu done")
        break

print("maximum memory usage: %.2f GB" % (max_mem_usage / 1024 / 1024))
print("maximum memory percent: %.2f" % (max_mem_usage / total_mem * 100) + "%")
