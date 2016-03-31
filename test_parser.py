from parser import Parser
import json

def test_parser():
    parse = Parser()
    parse.parse_message("I am @sam and here is a link: https://www.simple.com have a nice day (smiley).")
    expected = {"raw": "I am @sam and here is a link: https://www.simple.com have a nice day (smiley).", "mentions": ["sam"]}
    assert json.dumps(expected) == parse.to_json_str()

def test_extract_mentions():
    parse = Parser()
    msg = "@sam or hello @sam's fiancee is your name @katie? Or is it @katherine or whatever? is your email snkinard@gmail.com? also here is this thing @ "
    mentions = parse.extract_mentions(msg)
    assert 3 == len(mentions)
    assert "sam" in mentions
    assert "katie" in mentions
    assert "katherine" in mentions

def test_extract_emoticons():
    parse = Parser()
    msg = "(smiley) hey! (smiley2) hello(smiley_3)world (morethanfifteencharacters) (fifteencharactr) (lolol lolol) ((sam)) yeah) (yeah"
    emoticons = parse.extract_emoticons(msg)
    assert 5 == len(emoticons)
    assert "smiley" in emoticons
    assert "smiley2" in emoticons
    assert "smiley_3" in emoticons
    assert "fifteencharactr" in emoticons
    assert "sam" in emoticons

def test_extract_emoticons_goofy():
    parse = Parser()
    msg = "yeah) (yeah (sam)"
    emoticons = parse.extract_emoticons(msg)
    assert 1 == len(emoticons)
    assert "sam" in emoticons

def test_extract_links():
    parse = Parser()
