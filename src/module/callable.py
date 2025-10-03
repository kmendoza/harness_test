import time

import logging
logger = logging.getLogger(__name__)


class Foo:
    def __call__(self, *args):
        SEC = 100

        print(" ----> user task START")

        t0 = time.time()
        while 1 < 2:
            if time.time() - t0 > SEC:
                print(f"Finished running due to {time.time() - t0:.1f} s")
                break

        print("\n <---- DONE user task")

