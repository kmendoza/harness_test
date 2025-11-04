import os
import sys
import time


def foo():
    print("Entry point function foo")


class bar:
    def __call__(self, **kwargs):
        print("Entry point class bar")


if __name__ == "__main__":
    print("YEP. RUNNING entry point __main__")

    conda_env = os.environ.get("CONDA_DEFAULT_ENV")
    print(f"Current conda environment: {conda_env}")
    print(f"Python environment path: {sys.prefix}")
    for i in range(10):
        print(i)
        time.sleep(1)
