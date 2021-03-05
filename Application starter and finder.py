import os
import subprocess
import time

#
## START ALL APPLICATIONS
#

os.system("nohup spotify &") 
os.system("nohup rambox &")
os.system("nohup lutris &")
os.system("nohup firefox --new-window www.duck.com &")


time.sleep(15)

output = subprocess.run(["wmctrl", "-l"], capture_output=True)
print("\n\n")

s = output.stdout.decode('UTF-8')

processees = s.split("\n")
"""

for p in processees:
    foo = p.split(" ") 
    if (len(foo) < 4):
        continue
    id = foo[0]

    name_1 = foo[4]
    
    if (name_1 == "Spotify"):
        os.system(f"wmctrl -i -r {id} -N corner_spotify")
    if (name_1 == "Rambox"):
        os.system(f"wmctrl -i -r {id} -N corner_rambox")
    if (name_1 == "Lutris"):
        os.system(f"wmctrl -i -r {id} -N corner_lutris")




"""
spot_id = ""
ramb_id = ""
lutris_id = ""
firefox_id = ""




for p in processees:
    foo = p.split(" ") 
    if (len(foo) < 4):
        continue
    id = foo[0]

    name_1 = foo[4]
    
    if (name_1 == "Spotify"):
        spot_id = str(id)
    if (name_1 == "Rambox"):
        ramb_id = str(id)
    if (name_1 == "Lutris"):
        lutris_id = str(id)
    if (name_1 == "DuckDuckGo"):
        firefox_id = str(id)




load_settings = []
if (spot_id != ""):
    load_settings.append(f"spot_id: {spot_id}\n")
if (ramb_id != ""):
    load_settings.append(f"ramb_id: {ramb_id}\n")
if (lutris_id != ""):
    load_settings.append(f"lutris_id: {lutris_id}\n")
if (firefox_id != ""):
    load_settings.append(f"firefox_id: {firefox_id}\n")


f = open("/home/brendan/Documents/PythonScripts/wmctrl/session_info", "w")
f.writelines(load_settings)
f.close()



os.system("wmctrl -s 1")