#!/usr/bin/python3

from typing import List, Dict, Set
from typing import Any
import json

with open("../data/items_shuffle.json") as f:
    items: List[Dict[str, Any]] = json.load(f)

category_glossary: Dict[int, Set[str]] = {}

for itm in items:
    categories: List[str] = itm["product_category"].split("›")
    for i, ctgr in enumerate(categories):
        if i not in category_glossary:
            category_glossary[i] = set()
        category_glossary[i].add(ctgr.strip())

with open("categories.list", "w") as f:
    for i in sorted(category_glossary.keys()):
        f.write("[{:}]:\n".format(i))
        for ctgr in category_glossary[i]:
            f.write(ctgr + "\n")
        f.write("\n")
