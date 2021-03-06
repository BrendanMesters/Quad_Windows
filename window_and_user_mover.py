#! /usr/bin/python3

import os
import re
import subprocess
import time


def window_id_from_pid(pid = -1):
    assert (type(pid) == int), f"The PID is supposed to be an integer but was a `{type(pid)}` with value `{pid}`"
    call = ["wmctrl", "-lp"]
    proc = subprocess.run(call, capture_output=True)
    output = str(proc.stdout)
    
    # take off the binary tag that persists after the `str` call
    output = output[2 : -1]

    # loop over all lines (which are seperated by \\n instead of \n)
    # and split that line with the regex checking for one or more spaces
    # if the pid is the one we are looking for return its window_id.
    for l in output.split("\\n"):
        line_list = re.split("[ ]+", l)
        if (len(line_list) < 3): continue
        if (int(line_list[2]) == pid):
            return line_list[0]





#
########### THE CODE BELOW IS QUICKLY BODGED TO WORK WITH THE SYSTEM ABOVE
########### THIS CODE SHOULD BE CLEANED UP AND UPGRADED IN THE FUTURE
#




#constants
height = 490
spot_gxywh = [1, 0, 635, 924, 490]
ramb_gxywh = [7, 70, 0, 925, 490]
lutris_gxywh = [5, 1942, 1062, 975, 578]
firefox_gxywh = [3, 1007, 0, 923, 527]
used_desktop = 1


#reading in PIDs
f = open("/tmp/quadWindows_TEMP", "r")

spot_id = ""
ramb_id = ""
lutris_id = ""
firefox_id = ""

for l in f:
    parts = l.split(" ")
    if ("spot_id" in parts[0]):
        spot_id = int(parts[1])
    if ("ramb_id" in parts[0]):
        ramb_id = int(parts[1])
    if ("lutris_id" in parts[0]):
        lutris_id = int(parts[1])
    if ("firefox_id" in parts[0]):
        firefox_id = int(parts[1])

f.close()

spot_id = window_id_from_pid(spot_id)
ramb_id = window_id_from_pid(ramb_id)
lutris_id = window_id_from_pid(lutris_id)
firefox_id = window_id_from_pid(firefox_id)


def move_window(PID, gxywh, focus = False, desk = -1):
    # first unmaximize windows
    print(f" My PID is {PID}. and my gxywh is {gxywh}")
    os.system(f"wmctrl -i -r {PID} -b remove,maximized_vert; wmctrl -i -r {PID} -b remove,maximized_horz")
    
    #weird setup thing mostly for spotify
    os.system(f"wmctrl -i -r {PID} -e 0,563,415,924,490")
    
    # actual functionality
    os.system(f"wmctrl -i -r {PID} -e {gxywh[0]},{gxywh[1]},{gxywh[2]},{gxywh[3]},{gxywh[4]}")

    if (focus):
        os.system(f"wmctrl -i -a {PID}")
    if (desk != -1):
        os.system(f"wmctrl -i -r {PID} -t {desk}")


if (spot_id != ""):
    move_window(spot_id, spot_gxywh, focus = True, desk = used_desktop)
if (ramb_id != ""):
    move_window(ramb_id, ramb_gxywh, focus = True,  desk = used_desktop)
if (lutris_id != ""):
    move_window(lutris_id, lutris_gxywh, focus = True, desk = used_desktop)
if (firefox_id != ""):
    move_window(firefox_id, firefox_gxywh, focus = True, desk = used_desktop)


os.system(f"wmctrl -s {used_desktop}")