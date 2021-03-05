#! /usr/bin/python3

import os
import subprocess
import time



#constants
height = 490
spot_gxywh = [1, 0, 635, 924, 490]
ramb_gxywh = [7, 70, 0, 925, 490]
lutris_gxywh = [5, 1942, 1062, 975, 578]
firefox_gxywh = [3, 1007, 0, 923, 527]
used_desktop = 1


#reading in PIDs
f = open("/home/brendan/Documents/PythonScripts/wmctrl/session_info", "r")

spot_id = ""
ramb_id = ""
lutris_id = ""
firefox_id = ""

for l in f:
    parts = l.split(" ")
    if ("spot_id" in parts[0]):
        spot_id = int(parts[1], 16)
    if ("ramb_id" in parts[0]):
        ramb_id = int(parts[1], 16)
    if ("lutris_id" in parts[0]):
        lutris_id = int(parts[1], 16)
    if ("firefox_id" in parts[0]):
        firefox_id = int(parts[1], 16)

f.close()


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