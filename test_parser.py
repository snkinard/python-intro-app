from parser import Parser
import json
import pytest
import mechanize

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
    url1 = "https://inbox.google.com"
    url2 = "https://www.utexas.edu"
    url3 = "https://www.host.domain.com:80/path/page.php?query=value&a2=v2#foo"
    msg = "here is a link: {0} and two more {1} {2}".format(url1, url2, url3)
    parse = Parser()
    links = parse.extract_links(msg)
    assert 3 == len(links)
    assert url1 in links
    assert url2 in links
    assert url3 in links

def test_get_link_metadata(monkeypatch):

    url = "http://www.vinylmeplease.com"
    def mockopen(browser, link):
        assert url == link
        return None
    monkeypatch.setattr(mechanize.Browser, "open", mockopen)

    title = "Vinyl Me, Please"
    def mocktitle(browser):
        return title
    monkeypatch.setattr(mechanize.Browser, "title", mocktitle)

    links = ["http://www.vinylmeplease.com"]
    parse = Parser()
    browser = mechanize.Browser()
    meta_links = parse.get_link_metadata(links, browser)
    assert 1 == len(meta_links)
    link_hash = meta_links[0]
    assert "link" in link_hash
    assert url == link_hash["link"]
    assert "title" in link_hash
    assert title == link_hash["title"]
