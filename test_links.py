import links
import mechanize


def test_extract():
    url1 = "https://inbox.google.com"
    url2 = "https://www.utexas.edu"
    url3 = "https://www.host.domain.com:80/path/page.php?query=value&a2=v2#foo"
    msg = "here is a link: {0} and two more {1} {2}".format(url1, url2, url3)
    links_list = links.extract(msg)
    assert 3 == len(links_list)
    assert url1 in links_list
    assert url2 in links_list
    assert url3 in links_list


def test_get_metadata(monkeypatch):

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

    links_list = [url1, url2]
    meta_links = links.get_metadata(links_list, mechanize.Browser())
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


def test_get_link_metadata_open_error(monkeypatch):
    url = "https://www.betterment.com"

    def mockopen(browser, link):
        assert link == url
        # https://github.com/jjlee/mechanize/blob/master/mechanize/_mechanize.py#L255
        raise HTTPError("https://www.betterment.com", 403, "Forbidden", "", None)
    monkeypatch.setattr(mechanize.Browser, "open", mockopen)

    def mocktitle(browser):
        # don't want this method to be called if webpage was not opened
        assert False
    monkeypatch.setattr(mechanize.Browser, "title", mocktitle)

    links_list = [url]
    meta_links = links.get_metadata(links_list, mechanize.Browser())
    assert 1 == len(meta_links)

    link_hash = meta_links[0]
    assert "url" in link_hash
    assert url == link_hash["url"]
    assert "title" in link_hash
    assert None == link_hash["title"]


def test_get_link_metadata_title_error(monkeypatch):
    url = "https://www.betterment.com"

    def mockopen(browser, link):
        assert link == url
    monkeypatch.setattr(mechanize.Browser, "open", mockopen)

    def mocktitle(browser):
        # https://github.com/jjlee/mechanize/blob/master/mechanize/_mechanize.py#L448
        raise mechanize.BrowserStateError("not viewing any document")
    monkeypatch.setattr(mechanize.Browser, "title", mocktitle)

    links_list = [url]
    meta_links = links.get_metadata(links_list, mechanize.Browser())
    assert 1 == len(meta_links)

    link_hash = meta_links[0]
    assert "url" in link_hash
    assert url == link_hash["url"]
    assert "title" in link_hash
    assert None == link_hash["title"]
