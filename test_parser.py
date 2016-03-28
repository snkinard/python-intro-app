import parser from Parser

def test_parser():
    msg = "Sam"
    assert msg, Parser.parse_message(msg)
