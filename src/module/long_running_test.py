import datetime as dt
import os
import sys
import time


def xyz(**kwargs):

    conda_env = os.environ.get("CONDA_DEFAULT_ENV")
    print("------------------------")
    print(f"Current conda environment: {conda_env}")
    print(f"Python environment path: {sys.prefix}")
    print("------------------------")

    while 1 < 2:
        print(f"{dt.datetime.now().strftime('%Y%m%d-%H:%M:%S')} : running....")
        time.sleep(1)
