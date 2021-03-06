import os
import subprocess
import time

# Pleaser make sure that apps contains the name that you use to
# launch them from the terminal (aka `spotify` in bash launches spotify).

# note that their tmp variable name will not change automatically, though this shouldn't effect the functionality
apps = ["spotify", "rambox", "lutris", "firefox"]



PIDs = {}
for app in apps:
    call = ["nohup", "APP, MUST BE OVERWRITTEN", "&"]
    call[1] = app
    proc = subprocess.Popen(call)
    PIDs[app] = proc.pid


# store pids in file_buffer to write to file in the next part.
keys = PIDs.keys()
file_buffer = []
if ( apps[0] in keys): file_buffer.append(f"spot_id: {PIDs[apps[0]]}\n")
if ( apps[1] in keys): file_buffer.append(f"ramb_id: {PIDs[apps[1]]}\n")
if ( apps[2] in keys): file_buffer.append(f"lutris_id: {PIDs[apps[2]]}\n")
if ( apps[3] in keys): file_buffer.append(f"firefox_id: {PIDs[apps[3]]}\n")



f = open("/tmp/quadWindows_TEMP", "w")
f.writelines(file_buffer)
f.close()