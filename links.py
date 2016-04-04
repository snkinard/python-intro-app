import re
from sets import Set
"""Links Module

This module contains functionality useful in the parsing of link information from a chat message.
"""


def extract(msg):
    """Extract

    Extracts urls from the given msg identified using the regular expression defined in the url_regex() function below.

    Args:
        msg (str): The msg to extract urls from.

    Returns:
        List[str]: A list of all urls found in the message, represented as strings.
    """

    rgx = url_regex()
    found = re.findall(rgx, msg)
    links_set = Set()
    for link in found:
        # dunno if I like this. don't need seperate groups to make this work.
        links_set.add(link[0].strip())
    return list(links_set)


def get_metadata(links_list, browser):
    """Get Metadata

    Uses mechanize.Browser to crawl a given url(s) and return metadata.

    Args:
        links_list (List[str]): A list of urls represented by strings.
        browser (mechanize.Browser): The browser instance to be utilized for crawling web pages. Passed in as a parameter to facilitate mocking during testing.

    Returns:
        List[Dict]: A list of dicts containing meta information about the given url(s).
    """

    links_meta = []
    browser.set_handle_robots(False)
    for link in links_list:
        open_failed = False
        try:
            browser.open(link)
        except:
            open_failed = True

        if open_failed:
            links_meta.append({"url": link, "title": None})
        else:
            try:
                links_meta.append({"url": link, "title": browser.title()})
            except:
                links_meta.append({"url": link, "title": None})
    return links_meta


def url_regex():
    """Url Regex

    Generates and a regular expression to parse URLs. Mostly based on this stack overflow post: https://stackoverflow.com/questions/9760588/how-do-you-extract-a-url-from-a-string-using-python/31952097#31952097

    Returns:
        RegexObject: URL Regular Expression.
    """

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
