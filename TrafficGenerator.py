# ============================================ #
# Author: Matthew Duong 
# Random PCAP Traffic Generator

# Created: September 25th, 2024
# Last Updated: September 28th, 2024
# ============================================ #

from DateTimeFetching import *

import subprocess
import sys
import os
import random
import time


# Choose a random .pcap file and return as a string
def choose_randpcap():
    curr_pcap = random.choice(os.listdir(f"/home/cyber/pcaps"))
    return curr_pcap

# Run the selected .pcap through tcpreplay
def start_replay():
    
    replay_proc = subprocess.Popen(
        ["sudo", "-S", "tcpreplay", "-i", "enp3s0", "--topspeed", f"/home/cyber/pcaps/{choose_randpcap()}"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Periodic check every 10 seconds to see if the .pcap replay is finished
    while True:

        status = replay_proc.poll()

        if status is not None:

            print(f"[ {get_datestamp()} ][ {get_timestamp()} ] tcp replay complete!")

            stdout_data, stderr_data = replay_proc.communicate()

            if stdout_data:
                print("=== tcpreplay output ===")
                print(stdout_data)
            if stderr_data:
                print("=== tcpreplay errors ===")
                print(stderr_data)

            return status

        else:
            print(f"[ {get_datestamp()} ][ {get_timestamp()} ] not done yet, wait 10 seconds...")
        time.sleep(10)


if __name__ == "__main__":
    
    status = start_replay()
    sys.exit(status)

