# ============================================ #
# Author: Matthew Duong
# General Date + Timestamp Fetcher

# Created: September 25th, 2024
# Last Updated: September 25th, 2024
# ============================================ #

from datetime import date, datetime

# Fetch timestamp
def get_timestamp():
    timestamp = datetime.now().strftime("%H:%M:%S")
    return timestamp
# Fetch dashed timestamp for file names
def get_dashedtime():
    dashed_time = datetime.now().strftime("%H-%M-%S")
    return dashed_time


# Fetch date stamp
def get_datestamp():
    datestamp = date.today().strftime("%m-%d-%Y")
    return datestamp

