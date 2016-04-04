import re
from sets import Set


def extract(msg):
    rgx = r"\s@[a-zA-Z]+|\A@[a-zA-Z]+"
    found = re.findall(rgx, msg)
    mentions_set = Set()
    # set to remove dupes
    for mention in found:
        # remove whitespace and @ character
        mentions_set.add(mention.strip().replace("@", ""))
    return list(mentions_set)
