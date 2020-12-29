import subprocess
import os

curr_sink = subprocess.getoutput('pacmd list-sinks | grep -F "active port" | cut -d " " -f 3')

if curr_sink == "<analog-output-speaker>":
    os.system('pacmd set-sink-port 0 analog-output-headphones')

else:
    os.system('pacmd set-sink-port 0 analog-output-speaker')
