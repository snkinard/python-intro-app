import re
from sets import Set
"""Mentions Module

This module contains functionality useful in the parsing of mentions information from a chat message.
"""


def extract(msg):
    """Extract

    Extracts mentions identified using a regular expression from the given msg.

    Args:
        msg (str): The message to extract mentions from.

    Returns:
        List[str]: A list of all mentions found in the message, represented as strings.
    """
    rgx = r"\s@[a-zA-Z]+|\A@[a-zA-Z]+"
    found = re.findall(rgx, msg)
    mentions_set = Set()
    # set to remove dupes
    for mention in found:
        # remove whitespace and @ character
        mentions_set.add(mention.strip().replace("@", ""))
    return list(mentions_set)
