#!/usr/bin/python3

import requests
from typing import Dict
import lxml.html
import lxml.cssselect
import numpy as np

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

pub_to_mine: np.ndarray = np.full((500,), -1, dtype=np.int32)
for i in range(500):
    # TODO: Network Error Handling
    response: requests.Response = requests.get("http://3.83.245.205:3000/{:}".format(i))
    html: lxml.html.Element = lxml.html.fromstring(response.text)
    h4: lxml.html.Element = cssselector(html)[0]
    #print(h4.text)
    #text: str = "".join(h4.itertext(with_tail=False))
    text: str = list(h4)[0].tail
    text = text.rsplit(", and price lower than", maxsplit=1)[0]
    #print(text, my_instructions[text])
    #exit(0)
    pub_to_mine[i] = my_instructions[text]
