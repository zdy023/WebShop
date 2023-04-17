#!/usr/bin/python3

from typing import Dict, List
from typing import Any
import json

with open("../data/items_shuffle.json") as f:
    items: List[Dict[str, Any]] = json.load(f)

with open("../data/items_human_ins.json") as f:
    instructions: Dict[str, List[Dict[str, Any]]] = json.load(f)

with open("item_to_instructions.list", "w") as f:
    for itm in items:
        asin: str = itm["asin"]
        if asin in instructions:
            for anntt in instructions[asin]:
                f.write("{:}\n".format(anntt["instruction"]))
