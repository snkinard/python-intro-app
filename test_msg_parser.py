from msg_parser import MsgParser
from urllib2 import HTTPError
import json
import pytest
import mechanize


def test_parser(monkeypatch):

    url = "https://www.simple.com"

    def mockopen(browser, link):
        assert url == link
        return None
    monkeypatch.setattr(mechanize.Browser, "open", mockopen)

    title = "Simple | Online Banking With Automatic Budgeting & Savings"

    def mocktitle(browser):
        return title
    monkeypatch.setattr(mechanize.Browser, "title", mocktitle)

    parse = MsgParser()
    # hijack Browser instance so it can be mocked
    parse.browser = mechanize.Browser()
    parse.parse_message("I am @sam and here is a link: https://www.simple.com have a nice day (smiley).")
    expected = {"raw": "I am @sam and here is a link: https://www.simple.com have a nice day (smiley).", "mentions": ["sam"], "emoticons": ["smiley"], "links": [{"url": "https://www.simple.com", "title": "Simple | Online Banking With Automatic Budgeting & Savings"}]}
    assert json.dumps(expected) == parse.to_json_str()
