import logging
import time

from bqm.harness import Command, Cradle

logger = logging.getLogger(__name__)


class TestJob(Cradle):

    def run(self, *args):
        SEC = 10000

        logger.info(" ----> user task START")

        logger.info(f"task config: {self.get_config()}")

        i, t0, ii, t00 = 1, time.time(), 0, time.time()
        while 1 < 2:
            # print(".", end="")
            msg = self.get_msg()
            if msg:
                logger.info(f"received command: {msg}")
                if msg["cmd"] == Command.START:
                    logger.warning("Got START")

            # time.sleep(1)
            # if i % 5 == 0:
            #     print()
            if time.time() - t0 > SEC:
                logger.info(f"Finished running due to {time.time() - t0:.1f} s")
                break

            if time.time() - t00 > 5:
                t00 = time.time()
                ii += 1
                self.set_status(status={"ii": ii})

            i += 1
        # 1 / 0
        # raise Exception()
        logger.info(" <---- DONE user task")
