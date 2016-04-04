import json
import re
from sets import Set
import mechanize

import links
import emoticons
import mentions


class MsgParser(object):
    """The main class for the MsgParser package.
    """

    def __init__(self):
        self.contents = {}
        self.browser = mechanize.Browser()

    def parse_message(self, msg):
        """Parse a given message and extract and store metadata about the message.

        Args:
            msg (str): The msg to parse metadata from.

        Returns:
            None
        """
        self.contents = {"raw": msg}
        self.contents["mentions"] = mentions.extract(msg)
        self.contents["emoticons"] = emoticons.extract(msg)
        self.contents["links"] = links.get_metadata(links.extract(msg), self.browser)

    def to_json_str(self):
        """A string json representation of any metadata found using the parse_message() method.

        Returs:
            str: Json representing metadata about a message as a string.
        """
        return json.dumps(self.contents)
