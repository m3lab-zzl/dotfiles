# open h5 file with vitables on Windows
# pip install vitables # make sure it is MSV version
# vitables # collections.Iterable -> collections.abc.Iterable (vitables\utils.py)

import os
import sys

f = sys.argv[1]
# get h5 abspath
h5path = os.path.abspath(f)
print(h5path)
# open h5 with vitables
os.system("powershell.exe vitables {}".format(h5path))
input("press enter key to exit...")
