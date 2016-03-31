from parser import Parser

def test_parser():
    assert '{"raw": "I am Sam"}' == Parser.parse_message("I am Sam")
