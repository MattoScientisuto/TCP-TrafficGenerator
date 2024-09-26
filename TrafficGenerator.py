# ============================================ #
# Author: Matthew Duong 
# Random PCAP Traffic Generator

# Created: September 25th, 2024
# Last Updated: September 26th, 2024
# ============================================ #

from DateTimeFetching import *

import subprocess
import os
import random
import time

confirmation_file = os.path.expanduser("~/confirm.txt")

# Choose a random .pcap file and return as a string
def choose_randpcap():
    curr_pcap = random.choice(os.listdir(f"/home/{os.getlogin()}/pcaps"))
    return curr_pcap

# Run the selected .pcap through tcpreplay
def start_replay():
    
    replay_proc = subprocess.Popen(
        ["sudo", "-S", "tcpreplay", "-i", "enp3s0", "--topspeed", f"{choose_randpcap()}"],
        f'echo "Cron job executed at {get_timestamp()}" >> {confirmation_file}',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Periodic check every 5 seconds to see if the .pcap replay is finished
    while True:
        # print(choose_randpcap())
        status = replay_proc.poll() 
        
        if status is not None:
            print(f"[{get_timestamp()}] done")
            return status
        else:
            print(f"[{get_timestamp()}] not done, wait 5 seconds")
        time.sleep(5)


if __name__ == "__main__":
    
    start_replay()
