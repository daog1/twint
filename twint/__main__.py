#import sys
#sys.path.append("/Users/gotham/code/pysrc/twint/twint")
from twint.cli import main
import logging, os

_levels = {"info": logging.INFO, "debug": logging.DEBUG}

_level ="debug" #os.getenv("TWINT_DEBUG", "info")
_logLevel = _levels[_level]

if _level == "debug":
    logger = logging.getLogger()
    _output_fn = "twint.log"
    logger.setLevel(_logLevel)
    formatter = logging.Formatter("%(levelname)s:%(asctime)s:%(name)s %(module)s:%(lineno)d :%(message)s")

    fileHandler = logging.FileHandler(_output_fn)
    fileHandler.setLevel(_logLevel)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
if __name__ == "__main__":
    main()
