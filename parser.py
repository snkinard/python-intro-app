import json

class Parser(object):

    @staticmethod
    def parse_message(msg):
        contents = {"raw": msg}
        return json.dumps(contents)
