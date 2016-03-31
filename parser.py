import json
import re
from sets import Set

class Parser(object):

    def __init__(self):
        self.contents = {}

    def parse_message(self, msg):
        self.contents = {"raw": msg}
        self.contents["mentions"] = self.extract_mentions(msg)

    def to_json_str(self):
        return json.dumps(self.contents)

    def extract_mentions(self, msg):
        rgx = r"\s@[a-zA-Z]+|\A@[a-zA-Z]+"
        found = re.findall(rgx, msg)
        mentions = Set()
        # set to remove dupes
        for mention in found:
            # remove whitespace and @ character
            mentions.add(mention.strip().replace("@", ""))
        return list(mentions)
