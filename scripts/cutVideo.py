# mamba install ffmpeg -c conda-forge
import os

from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyCompleter
from prompt_toolkit.completion.filesystem import PathCompleter

completer = FuzzyCompleter(PathCompleter())  # list completion


# check if ffmpeg is ready to use in command line, quiet mode
def must_be_file(hint):
    while True:
        user_input: str = prompt(hint, completer=completer).strip()
        if os.path.isfile(user_input):
            return user_input
        else:
            print("file not exist!")


def until_valid(hint):
    while True:
        user_input = input(hint).strip()
        time_list = user_input.split(" ")
        flag = True
        for time in time_list:
            if time == "":
                pass
            elif time.isdigit() and 0 <= int(time) <= 60:
                pass
            else:
                print("format error!")
                flag = False
        if flag:
            return user_input


fpath = must_be_file("filepath: ")
absfpath = os.path.abspath(fpath)
fname = os.path.basename(absfpath)
outname = input("output filename (defaults to trimmed_*): ")
if outname == "":
    trimmed_fname = "trimmed_" + fname
else:
    trimmed_fname = outname
assert not os.path.isfile(trimmed_fname), f"{trimmed_fname} already exist!"

st_str = until_valid("start point (format: 02 03 04): ")
st_list = st_str.split(" ")
if len(st_list) == 1:
    if st_list[0] == "":
        st_hour_min_sec = "00:00:00"
    else:
        st_hour_min_sec = "00:00:" + st_list[0]
elif len(st_list) == 2:
    st_hour_min_sec = "00:" + st_list[0] + ":" + st_list[1]
else:
    st_hour_min_sec = st_list[0] + ":" + st_list[1] + ":" + st_list[2]

et_str = until_valid("end point (format: 02 03 04): ")
et_list = et_str.split(" ")
if len(et_list) == 1:
    if et_list[0] == "":
        # get the duration of the video
        total_seconds_str = os.popen(
            f"ffprobe {absfpath} -show_entries format=duration -of compact=p=0:nk=1 -v 0"
        ).readlines()[0]
        total_seconds = float(total_seconds_str)
        et_hour_min_sec = (
            str(int(total_seconds // 3600))
            + ":"
            + str(int(total_seconds % 3600 // 60))
            + ":"
            + str(int(total_seconds % 60))
        )
    else:
        et_hour_min_sec = "00:00:" + et_list[0]
elif len(et_list) == 2:
    et_hour_min_sec = "00:" + et_list[0] + ":" + et_list[1]
else:
    et_hour_min_sec = et_list[0] + ":" + et_list[1] + ":" + et_list[2]

# cut video from start point to end point
print(
    f"$ ffmpeg -i {absfpath} -ss {st_hour_min_sec} -to {et_hour_min_sec} -c copy {trimmed_fname}\n converting with above command in quiet mode..."
)
os.system(
    f"ffmpeg -i {absfpath} -ss {st_hour_min_sec} -to {et_hour_min_sec} -c copy {trimmed_fname} > ffmpeg_log.txt 2>&1"
)
if os.path.isfile(trimmed_fname):
    print(f"==> check {trimmed_fname}!")
else:
    print("==> something wrong, check ffmpeg_log.txt for details!")
input("press any key to exit...")
