import json
import re
from sets import Set
import mechanize

class MsgParser(object):

    def __init__(self):
        self.contents = {}

    def parse_message(self, msg):
        self.contents = {"raw": msg}
        self.contents["mentions"] = self.extract_mentions(msg)
        self.contents["emoticons"] = self.extract_emoticons(msg)
        browser = mechanize.Browser()
        self.contents["links"] = self.get_link_metadata(self.extract_links(msg), browser)

    def to_json_str(self):
        return json.dumps(self.contents)

    def extract_mentions(self, msg):
        rgx = r"\s@[a-zA-Z]+|\A@[a-zA-Z]+"
        found = re.findall(rgx, msg)
        mentions = Set()
        # set to remove dupes
        for mention in found:
            # remove whitespace and @ character
            mentions.add(mention.strip().replace("@", ""))
        return list(mentions)

    def extract_emoticons(self, msg):
        rgx = r"\(\w{1,15}\)"
        found = re.findall(rgx, msg)
        emoticons = Set()
        for emoticon in found:
            emoticons.add(emoticon[1:-1])
        return list(emoticons)

    def get_link_metadata(self, links, browser):
        links_meta = []
        for link in links:
            browser.set_handle_robots(False)
            # error handling?
            browser.open(link)
            links_meta.append({"url": link, "title": browser.title()})
        return links_meta

    def extract_links(self, msg):
        rgx = self.url_regex()
        found = re.findall(rgx, msg)
        links = Set()
        for link in found:
            # dunno if I like this. don't need seperate groups to make this work.
            links.add(link[0].strip())
        return list(links)

    # full disclosure, mostly yanked from here: https://stackoverflow.com/questions/9760588/how-do-you-extract-a-url-from-a-string-using-python/31952097#31952097
    def url_regex(self):
        regex = r'('

        # Scheme (HTTP, HTTPS, FTP and SFTP):
        regex += r'(?:(https?|s?ftp):\/\/)?'

        # www:
        regex += r'(?:www\.)?'

        regex += r'('

        # Host and domain (including ccSLD):
        regex += r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+)'

        # TLD:
        regex += r'([A-Z]{2,6})'

        # IP Address:
        regex += r'|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

        regex += r')'

        # Port:
        regex += r'(?::(\d{1,5}))?'

        # Query path:
        regex += r'(?:(\/\S+)*)'

        regex += r')'

        return re.compile(regex, re.IGNORECASE)
