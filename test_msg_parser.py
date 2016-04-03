from msg_parser import MsgParser
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
    expected = {"raw": "I am @sam and here is a link: https://www.simple.com have a nice day (smiley).", "mentions": ["sam"], "emoticons": ["smiley"], "links":[{"url": "https://www.simple.com", "title":"Simple | Online Banking With Automatic Budgeting & Savings"}]}
    assert json.dumps(expected) == parse.to_json_str()

def test_extract_mentions():
    parse = MsgParser()
    msg = "@sam or hello @sam's fiancee is your name @katie? Or is it @katherine or whatever? is your email snkinard@gmail.com? also here is this thing @ "
    mentions = parse.extract_mentions(msg)
    assert 3 == len(mentions)
    assert "sam" in mentions
    assert "katie" in mentions
    assert "katherine" in mentions

def test_extract_emoticons():
    parse = MsgParser()
    msg = "(smiley) hey! (smiley2) hello(smiley_3)world (morethanfifteencharacters) (fifteencharactr) (lolol lolol) ((sam)) yeah) (yeah"
    emoticons = parse.extract_emoticons(msg)
    assert 5 == len(emoticons)
    assert "smiley" in emoticons
    assert "smiley2" in emoticons
    assert "smiley_3" in emoticons
    assert "fifteencharactr" in emoticons
    assert "sam" in emoticons

def test_extract_emoticons_goofy():
    parse = MsgParser()
    msg = "yeah) (yeah (sam)"
    emoticons = parse.extract_emoticons(msg)
    assert 1 == len(emoticons)
    assert "sam" in emoticons

def test_extract_links():
    url1 = "https://inbox.google.com"
    url2 = "https://www.utexas.edu"
    url3 = "https://www.host.domain.com:80/path/page.php?query=value&a2=v2#foo"
    msg = "here is a link: {0} and two more {1} {2}".format(url1, url2, url3)
    parse = MsgParser()
    links = parse.extract_links(msg)
    assert 3 == len(links)
    assert url1 in links
    assert url2 in links
    assert url3 in links

def test_get_link_metadata(monkeypatch):

    url1 = "http://www.vinylmeplease.com"
    url2 = "https://www.betterment.com"
    def mockopen(browser, link):
        if (url1 != link) & (url2 != link):
            assert False
    monkeypatch.setattr(mechanize.Browser, "open", mockopen)

    title = "A Website Title"
    def mocktitle(browser):
        return title
    monkeypatch.setattr(mechanize.Browser, "title", mocktitle)

    links = [url1, url2]
    parse = MsgParser()
    # hijack Browser instance so it can be mocked
    parse.browser = mechanize.Browser()
    meta_links = parse.get_link_metadata(links)
    assert 2 == len(meta_links)

    link_hash = meta_links[0]
    assert "url" in link_hash
    assert url1 == link_hash["url"]
    assert "title" in link_hash
    assert title == link_hash["title"]

    link_hash = meta_links[1]
    assert "url" in link_hash
    assert url2 == link_hash["url"]
    assert "title" in link_hash
    assert title == link_hash["title"]
