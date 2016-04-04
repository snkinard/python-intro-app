import re
from sets import Set


def extract(msg):
    rgx = r"\(\w{1,15}\)"
    found = re.findall(rgx, msg)
    emoticons_set = Set()
    for emoticon in found:
        emoticons_set.add(emoticon[1:-1])
    return list(emoticons_set)
