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

    def extract_emoticons(self, msg):
        rgx = r"\(\w{1,15}\)"
        found = re.findall(rgx, msg)
        emoticons = Set()
        for emoticon in found:
            emoticons.add(emoticon[1:-1])
        return list(emoticons)

    def extract_links(self, msg):
        return []
