import json
import nonebot

TOOLS = nonebot.get_driver().config.tools_path
DATA = TOOLS[:TOOLS.find("/tools")]+"/data"

def already_married(obj, group: str): # 是不是已经结婚了，噔噔咚
    cache = open(DATA + "/" + group + "/marry.json", mode="r")
    marrylist = json.loads(cache.read())
    cache.close()
    for i in marrylist:
        if i["wife"] == obj or i["husband"] == obj:
            return True
        else:
            continue
    return False