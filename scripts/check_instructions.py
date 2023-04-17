#!/usr/bin/python3

import sys
sys.path.append("..")

import importlib
importlib.import_module("web_agent_site.envs")
import gym

import json
from typing import Dict, List
from typing import Union
import itertools

#  Env, No Human Goals {{{ # 
#env = gym.make( "WebAgentTextEnv-v0"
              #, observation_mode="text_rich"
              #, human_goals=False
              #) # 6910 goals/1167 4685 goals
#
#with open("env.nohuman.list", "w") as f:
    #for i in range(6910):
        #env.reset(session=i)
        #f.write(env.get_instruction_text() + "\n")
#  }}} Env, No Human Goals # 

#  Env, With Human Goals {{{ # 
env = gym.make( "WebAgentTextEnv-v0"
              , observation_mode="text_rich"
              , human_goals=True
              ) # 13 goals/1 2087 goals

with open("env.human.list", "w") as f:
    for i in range(1_2087):
        env.reset(session=i)
        f.write(env.get_instruction_text() + "\n")
#  }}} Env, With Human Goals # 

#  data/items_human_ins.json {{{ # 
with open("../data/items_human_ins.json") as f:
    data: Dict[ str
              , List[ Dict[ str
                          , Union[ str
                                 , List[str]
                                 ]
                          ]
                    ]
              ] = json.load(f)

with open("data.human_ins.list", "w") as f:
    for itm in itertools.chain.from_iterable(data.values()):
        f.write(itm["instruction"] + "\n")
#  }}} data/items_human_ins.json # 

#  data/items_ins_v2_1000.json {{{ # 
with open("../data/items_ins_v2_1000.json") as f:
    data: Dict[ str
              , Dict[ str
                    , Union[ str
                           , List[str]
                           ]
                    ]
              ] = json.load(f)

with open("data.ins_v2.1000.list", "w") as f:
    for itm in data.values():
        if "instruction" in itm:
            f.write(itm["instruction"] + "\n")
#  }}}  data/items_ins_v2_1000.json # 

#  data/items_ins_v2.json {{{ # 
with open("../data/items_ins_v2.json") as f:
    data: Dict[ str
              , Dict[ str
                    , Union[ str
                           , List[str]
                           ]
                    ]
              ] = json.load(f)

with open("data.ins_v2.list", "w") as f:
    for itm in data.values():
        if "instruction" in itm:
            f.write(itm["instruction"] + "\n")
#  }}}  data/items_ins_v2.json # 

#  baseline_models/data/human_goals.json {{{ # 
with open("../baseline_models/data/human_goals.json") as f:
    data: List[str] = json.load(f)

with open("base.data.human_goals.list", "w") as f:
    for itm in data:
        f.write(itm + "\n")
#  }}} baseline_models/data/human_goals.json # 

#  baseline_models/data/items_human_ins.json {{{ # 
with open("../baseline_models/data/items_human_ins.json") as f:
    data: Dict[ str
              , List[ Dict[ str
                          , Union[ str
                                 , List[str]
                                 ]
                          ]
                    ]
              ] = json.load(f)

with open("base.data.human_ins.list", "w") as f:
    for itm in itertools.chain.from_iterable(data.values()):
        f.write(itm["instruction"] + "\n")
#  }}} baseline_models/data/items_human_ins.json # 
