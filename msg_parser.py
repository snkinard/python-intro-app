import json
import re
from sets import Set
import mechanize

import links
import emoticons
import mentions


class MsgParser(object):

    def __init__(self):
        self.contents = {}
        self.browser = mechanize.Browser()

    def parse_message(self, msg):
        self.contents = {"raw": msg}
        self.contents["mentions"] = mentions.extract(msg)
        self.contents["emoticons"] = emoticons.extract(msg)
        self.contents["links"] = links.get_metadata(links.extract(msg), self.browser)

    def to_json_str(self):
        return json.dumps(self.contents)
