import re
from sets import Set


def extract(msg):
    """Extract

    Extracts emoticons matching a regular expression from the given message.

    Args:
        msg (str): The message to extract emoticons from.

    Returns:
        List[str]: A list of all emoticons found in the message, represented as strings.
    """
    rgx = r"\(\w{1,15}\)"
    found = re.findall(rgx, msg)
    emoticons_set = Set()
    for emoticon in found:
        emoticons_set.add(emoticon[1:-1])
    return list(emoticons_set)
