import re
from sets import Set


def extract(msg):
    rgx = url_regex()
    found = re.findall(rgx, msg)
    links_set = Set()
    for link in found:
        # dunno if I like this. don't need seperate groups to make this work.
        links_set.add(link[0].strip())
    return list(links_set)


def get_metadata(links_list, browser):
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


# full disclosure, mostly yanked from here: https://stackoverflow.com/questions/9760588/how-do-you-extract-a-url-from-a-string-using-python/31952097#31952097
def url_regex():
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
