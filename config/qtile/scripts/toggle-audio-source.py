import subprocess
import os

curr_source = subprocess.getoutput('pacmd list-sources | grep -F "active port" | cut -d " " -f 3')

if curr_source == "<analog-input-internal-mic>":
    os.system('pacmd set-source-port 1 analog-input-headset-mic')

else:
    os.system('pacmd set-source-port 1 analog-input-internal-mic')
