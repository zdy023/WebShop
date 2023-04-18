#!/usr/bin/python3

import requests
from typing import Dict
import lxml.html
import lxml.cssselect
import numpy as np
import logging
import traceback
import datetime
import os
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

datetime_str: str = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")

file_handler = logging.FileHandler(os.path.join("logs-align/", "normal-{:}.log".format(datetime_str)))
debug_handler = logging.FileHandler(os.path.join("logs-align/", "debug-{:}.log".format(datetime_str)))
stdout_handler = logging.StreamHandler(sys.stdout)
sdebug_handler = logging.FileHandler(os.path.join("logs-align/", "sdebug-{:}.log".format(datetime_str)))

file_handler.setLevel(logging.INFO)
debug_handler.setLevel(logging.DEBUG)
stdout_handler.setLevel(logging.INFO)
sdebug_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt="\x1b[1;33m[%(asctime)s \x1b[31m%(levelname)s \x1b[32m%(module)s/%(lineno)d-%(processName)s\x1b[1;33m] \x1b[0m%(message)s")
file_handler.setFormatter(formatter)
debug_handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)
sdebug_handler.setFormatter(formatter)

stdout_handler.addFilter(logging.Filter("main"))
sdebug_handler.addFilter(logging.Filter("main"))

logger.addHandler(file_handler)
logger.addHandler(debug_handler)
logger.addHandler(stdout_handler)
logger.addHandler(sdebug_handler)

logger = logging.getLogger("main")

with open("env.human.list") as f:
    my_instructions: Dict[str, int] = { instrct: i for i, instrct in\
                                        enumerate( map( lambda l: l.strip()\
                                                                   .rsplit( ", and price lower than"
                                                                          , maxsplit=1
                                                                          )\
                                                                   [0]
                                                      , f.readlines()
                                                      )
                                                 )
                                      }

cssselector = lxml.cssselect.CSSSelector("h4", translator="html")

start_size = 500
max_size = 600
pub_to_mine: np.ndarray = np.full((max_size,), -1, dtype=np.int32)
for i in range(start_size, max_size):
    try:
        response: requests.Response = requests.get( "http://3.83.245.205:3000/{:}".format(i)
                                                  , timeout=10
                                                  )
        html: lxml.html.Element = lxml.html.fromstring(response.text)
        h4: lxml.html.Element = cssselector(html)[0]

        text: str = list(h4)[0].tail
        text = text.rsplit(", and price lower than", maxsplit=1)[0]
        logger.debug("#%d, %s, @%d", i, text, my_instructions[text])

        pub_to_mine[i] = my_instructions[text]
    except requests.Timeout:
        traceback.print_exc()
        logger.error("Fetching Pub#%d timeouted!", i)
    except requests.ConnectionError:
        traceback.print_exc()
        logger.error("Connection error during fetching Pub#%d!", i)

with open("pub-to-mine.list", "a") as f:
    for i in pub_to_mine[start_size:]:
        f.write("{:d}\n".format(i))
